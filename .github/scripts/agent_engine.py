import os
from google import genai
from google.genai import types

def main():
    # 1. Fetch environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    issue_title = os.environ.get("ISSUE_TITLE", "")
    issue_body = os.environ.get("ISSUE_BODY", "")
    
    if not api_key:
        print("Missing GEMINI_API_KEY secret.")
        return

    # 2. Read current application state
    with open("index.html", "r", encoding="utf-8") as f:
        current_code = f.read()
    with open("roadmap.md", "r", encoding="utf-8") as f:
        current_roadmap = f.read()

    # 3. Construct the prompt for the autonomous agent
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
    4. Return your response in strict JSON format with exactly two keys: "html" and "roadmap". Do not include Markdown code blocks inside the JSON fields.
    """

    # 4. Call the LLM
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2
        )
    )

    # 5. Parse output and overwrite repository files natively
    import json
    result = json.loads(response.text)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(result["html"])
        
    with open("roadmap.md", "w", encoding="utf-8") as f:
        f.write(result["roadmap"])

    print("Codebase successfully iterated by AI Agent.")

if __name__ == "__main__":
    main()
