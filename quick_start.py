import requests
import json

# Configuration
api_endpoint = "[ ENTER_CHAT_URL_HERE ]"
api_key = "[ ENTER_API_KEY_HERE ]"
model = "gpt-4.1"
prompt = "Explain the benefits of AI in business."

# Request
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
data = {
    "model": model,
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 500,
    "temperature": 0.7,
    "stream": True,
}

response = requests.post(
    f"{api_endpoint}/chat/completions", headers=headers, json=data, stream=True
)

# Process response
if response.status_code == 200:
    for line in response.iter_lines(decode_unicode=True):
        if line and line.startswith("data: "):
            data_str = line[6:]
            if data_str.strip() == "[DONE]":
                break
            try:
                data = json.loads(data_str)
                if "choices" in data and data["choices"]:
                    delta = data["choices"][0].get("delta", {})
                    if "content" in delta:
                        print(delta["content"], end="", flush=True)
            except:
                continue
    print("\n")
else:
    print(f"Error: {response.status_code}")
