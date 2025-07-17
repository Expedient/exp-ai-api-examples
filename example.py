"""
AI API Streaming Example - Python Client
========================================

This script demonstrates how to make streaming API calls to the Expedient AI Chat API.
It shows real-time response processing for a better user experience.

For complete API documentation and Postman examples, see postman.md
For project overview and setup instructions, see README.md
For a minimal version without comments, see quick_start.py
"""

# Import required libraries for HTTP requests and JSON processing
import requests  # For making HTTP API calls
import json  # For parsing JSON data from streaming responses

# =============================================================================
# API CONFIGURATION
# =============================================================================

# Define the base API endpoint for the Expedient AI Chat service
api_endpoint = "[ ENTER_CHAT_URL_HERE ]"

# Set your API authentication key (replace with your actual key)
# This key authorizes your requests to the AI service
api_key = "[ ENTER_API_KEY_HERE ]"  # Replace with your actual API key

# Specify which AI model to use for generating responses
# Choose from multiple AI providers based on your needs:

# Standard Models (recommended for general use)
model = "gpt-4.1"  # Latest general AI model (default)

# Alternative model options (uncomment to use):

# OpenAI Models:
# model = "gpt-4o"                               # Advanced GPT-4 model
# model = "gpt-4o-mini"                          # Faster, more cost-effective
# model = "gpt-3.5-turbo"                        # Fast and efficient

# Claude Models (Anthropic):
# model = "claude-3-7-sonnet-20250219"  # Claude 3.7 Sonnet (proven)
# model = "claude-3-haiku-20240307"              # Fast Claude model

# Gemini Models (Google):
# model = "gemini/gemini-2.0-flash"  # Faster Gemini model
# model = "gemini/gemini-1.5-flash-8b"           # Smaller and faster Gemini model

# Perplexity Models (Web-connected):
# NOTE: Your AI account must have web access models enabled.
# model = "perplexity/sonar-pro"                 # Web access with enhanced capabilities
# model = "perplexity/sonar"                     # Standard web-connected model

# For reasoning models, see reasoning_example.py
# For web reasoning with citations, see citation_example.py

# Define the prompt/question you want to ask the AI
# This is the user input that will be sent to the AI model
prompt = "Summarize the key benefits of enterprise AI adoption."

# =============================================================================
# REQUEST PREPARATION
# =============================================================================

# Set up HTTP headers required for the API request
# Content-Type tells the server we're sending JSON data
# Authorization provides the API key for authentication
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

# Create the request payload (data to send to the API)
data = {
    "model": model,  # Which AI model to use
    "messages": [{"role": "user", "content": prompt}],  # Conversation messages array
    "max_tokens": 1000,  # Maximum length of AI response (adjust as needed)
    "temperature": 0.7,  # Controls creativity (0.0=deterministic, 1.0=creative)
    "stream": True,  # Enable streaming for real-time responses
}

# Construct the complete API URL by combining base endpoint with the chat completions path
api_full = f"{api_endpoint}/chat/completions"

# =============================================================================
# API REQUEST EXECUTION
# =============================================================================

# Make the HTTP POST request to the AI API with streaming enabled
# stream=True allows us to process responses in real-time as they arrive
response = requests.post(api_full, headers=headers, json=data, stream=True, timeout=120)

# =============================================================================
# RESPONSE PROCESSING
# =============================================================================

# Check if the API request was successful (HTTP 200 OK status)
if response.status_code == 200:
    print("AI Response (streaming):")
    print("-" * 50)

    # Process the streaming response line by line
    for line in response.iter_lines(decode_unicode=True):
        if line and line.startswith("data: "):
            data_str = line[6:]  # Remove 'data: ' prefix

            # Check for completion signal
            if data_str.strip() == "[DONE]":
                break

            # Parse and display content
            try:
                data = json.loads(data_str)
                if "choices" in data and data["choices"]:
                    delta = data["choices"][0].get("delta", {})
                    if "content" in delta:
                        print(delta["content"], end="", flush=True)
            except json.JSONDecodeError:
                continue  # Skip malformed JSON

    print("\n" + "-" * 50)
    print("Stream completed.")

else:
    # Handle API request failures by displaying error information
    # This helps with debugging authentication, network, or server issues
    print(f"Request failed: {response.status_code}, {response.text}")
