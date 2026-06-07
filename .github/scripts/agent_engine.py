import os
import json
import time
from google import genai
from google.genai import types

def clean_json_string(text):
    """Strips markdown code block wrappers if the AI accidentally includes them."""
    text = text.strip()
    if text.startswith("```"):
        # Remove opening lines like ```json or ```
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline:].strip()
        # Remove closing lines like ```
        if text.endswith("```"):
            text = text[:-3].strip()
    return text

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    issue_title = os.environ.get("ISSUE_TITLE", "")
    issue_body = os.environ.get("ISSUE_BODY", "")
    
    if not api_key:
        print("❌ Error: Missing GEMINI_API_KEY secret in GitHub settings.")
        exit(1)

    # 1. Read the current repository state
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            current_code = f.read()
        with open("roadmap.md", "r", encoding="utf-8") as f:
            current_roadmap = f.read()
    except Exception as e:
        print(f"❌ Error reading codebase files: {e}")
        exit(1)

    # 2. Construct the systemic engineering prompt
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
    4. Return your response in a clear JSON structure containing exactly two keys: "html" and "roadmap". Do not include Markdown code blocks inside the JSON fields.
    """

    # 3. Call the Gemini API with an automatic retry loop for resilience
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
                    response_mime_type="application/json",
                    temperature=0.2
                )
            )
            raw_text = response.text
            break  # Success, exit the retry loop
            
        except Exception as e:
            error_msg = str(e)
            # Check for common temporary server or rate limit errors
            if "503" in error_msg or "429" in error_msg or "UNAVAILABLE" in error_msg:
                print(f"⚠️ Server is currently congested or rate-limited. Retrying in {delay_seconds} seconds...")
                time.sleep(delay_seconds)
                # Double the wait time for the next attempt (exponential backoff)
                delay_seconds *= 2 
            else:
                print(f"❌ Unrecoverable API error encountered: {e}")
                exit(1)

    if not raw_text:
        print(f"❌ Gemini API Call failed after {max_retries} attempts due to server availability.")
        exit(1)

    # 4. Sanitize and parse JSON safely
    try:
        cleaned_text = clean_json_string(raw_text)
        result = json.loads(cleaned_text)
        
        if "html" not in result or "roadmap" not in result:
            raise KeyError("Missing required keys 'html' or 'roadmap' in AI response.")
            
    except Exception as e:
        print("❌ Failed to parse JSON from AI response.")
        print(f"Parsing Error: {e}")
        print("--- RAW AI RESPONSE START ---")
        print(raw_text)
        print("--- RAW AI RESPONSE END ---")
        exit(1)

    # 5. Overwrite files locally for the GitHub Action to commit
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(result["html"])
            
        with open("roadmap.md", "w", encoding="utf-8") as f:
            f.write(result["roadmap"])
        print("✅ Codebase successfully iterated by AI Agent.")
    except Exception as e:
        print(f"❌ Failed to write updated files to workspace: {e}")
        exit(1)

if __name__ == "__main__":
    main()
