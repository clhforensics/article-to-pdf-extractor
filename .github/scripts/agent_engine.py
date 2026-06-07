import os
import re
import time
from google import genai
from google.genai import types

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    issue_title = os.environ.get("ISSUE_TITLE", "")
    issue_body = os.environ.get("ISSUE_BODY", "")
    
    if not api_key:
        print("❌ Error: Missing GEMINI_API_KEY secret in GitHub settings.")
        exit(1)

    try:
        with open("index.html", "r", encoding="utf-8") as f:
            current_code = f.read()
        with open("roadmap.md", "r", encoding="utf-8") as f:
            current_roadmap = f.read()
    except Exception as e:
        print(f"❌ Error reading codebase files: {e}")
        exit(1)

    prompt = f"""
    You are an autonomous senior software engineer. Your task is to update a single-file application based on a GitHub issue.
    
    Task: {issue_title}
    Details: {issue_body}
    
    Current roadmap context:
    {current_roadmap}
    
    Current source code:
    {current_code}
    
    Instructions:
    1. Implement the requested changes perfectly inside the single-file HTML/JS structure.
    2. Maintain the zero-dependency, pure vanilla JS architecture.
    3. Update the `roadmap.md` file by marking the implemented feature as completed '[x]'.
    
    CRITICAL FORMATTING INSTRUCTION:
    Do not use JSON. You must return exactly two markdown code blocks.
    First, the updated HTML file wrapped in ```html ... ```
    Second, the updated roadmap wrapped in ```markdown ... ```
    """

    raw_text = None
    max_retries = 3
    delay_seconds = 15

    for attempt in range(max_retries):
        print(f"🤖 Sending request to Gemini (Attempt {attempt + 1}/{max_retries})...")
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2
                )
            )
            raw_text = response.text
            break
        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "429" in error_msg or "UNAVAILABLE" in error_msg:
                print(f"⚠️ Server busy. Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds)
                delay_seconds *= 2 
            else:
                print(f"❌ Unrecoverable API error: {e}")
                exit(1)

    if not raw_text:
        print(f"❌ Gemini API Call failed after {max_retries} attempts.")
        exit(1)

    # Robust Markdown Extraction
    try:
        html_match = re.search(r'```html\n(.*?)\n```', raw_text, re.DOTALL)
        md_match = re.search(r'```markdown\n(.*?)\n```', raw_text, re.DOTALL)
        
        if not html_match or not md_match:
            raise ValueError("AI failed to return the requested markdown blocks.")
            
        new_html = html_match.group(1).strip()
        new_roadmap = md_match.group(1).strip()
        
    except Exception as e:
        print("❌ Failed to extract code from AI response.")
        print(f"Extraction Error: {e}")
        exit(1)

    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_html)
            
        with open("roadmap.md", "w", encoding="utf-8") as f:
            f.write(new_roadmap)
        print("✅ Codebase successfully iterated by AI Agent.")
    except Exception as e:
        print(f"❌ Failed to write updated files to workspace: {e}")
        exit(1)

if __name__ == "__main__":
    main()
