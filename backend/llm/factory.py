import requests
import json
from config import Config

def get_llm_response(prompt: str) -> str:
    # Build request body by replacing {prompt} in the template
    try:
        request_body = Config.LLM_REQUEST_BODY_TEMPLATE
        if not request_body:
            return "Request body template is empty."
        request_body = json.loads(request_body)
        request_body['contents'][0]['parts'][0]['text'] = prompt
        # request_body = json.loads(request_body)  # Parse JSON string to dict
    except Exception as e:
        return f"Error in request template: {str(e)}"

    # Prepare headers with dynamic API key header and optional prefix
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": "GEMINI_API_KEY"
    }

    # Only add API key if header is not set to "skip"
    if Config.LLM_API_KEY_HEADER.lower() != "skip":
        headers[Config.LLM_API_KEY_HEADER] = f"{Config.LLM_API_KEY_PREFIX} {Config.LLM_API_KEY}".strip()

    # Make the POST request
    try:
        response = requests.request(
            method=Config.LLM_API_METHOD.upper(),
            url=Config.LLM_API_URL,
            headers=headers,
            json=request_body
        )
        response.raise_for_status()
    except Exception as e:
        return f"LLM request failed: {str(e)}"

    # Extract response using dot notation path (simple implementation)
    try:
        result = response.json()
        for key in Config.LLM_RESPONSE_JSON_PATH.split('.'):
            if key.isdigit():
                result = result[int(key)]
            else:
                result = result[key]
        return result
    except Exception as e:
        return f"Failed to parse LLM response: {str(e)}"
