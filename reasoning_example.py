"""
AI API Reasoning Models Example - Python Client
===============================================

This script demonstrates how to use reasoning-capable AI models that can "think"
through complex problems step by step. These models require special parameters
and are best suited for complex analysis, logic puzzles, and multi-step reasoning.

For complete API documentation and Postman examples, see postman.md
For standard streaming models, see example.py
"""

# Import required libraries for HTTP requests and JSON processing
import requests  # For making HTTP API calls
import json  # For parsing JSON data from streaming responses
import threading  # For animated thinking dots
import time  # For timing the dot animation

# =============================================================================
# ANIMATED THINKING INDICATOR
# =============================================================================


def animate_thinking():
    """Show animated dots while AI is thinking"""
    dots = [".", "..", "..."]
    i = 0
    while thinking_active:
        print(f"\r🤔 AI is thinking{dots[i % 3]}   ", end="", flush=True)
        time.sleep(0.5)  # Update every 0.5 seconds
        i += 1


# =============================================================================
# API CONFIGURATION
# =============================================================================

# Define the base API endpoint for the Expedient AI Chat service
api_endpoint = "[ ENTER_CHAT_URL_HERE ]"

# Set your API authentication key (replace with your actual key)
# This key authorizes your requests to the AI service
api_key = "[ ENTER_API_KEY_HERE ]"  # Replace with your actual API key

# Reasoning Models (require special parameters)
# These models can "think" through problems step by step

model = "o4-mini"  # OpenAI reasoning model (recommended)

# Alternative reasoning model options (uncomment to use):

# OpenAI Reasoning Models:
# model = "o3"                                   # Latest OpenAI reasoning model

# Claude Reasoning Models:
# model = "claude-sonnet-4-20250514"             # Latest Claude 4 Sonnet with reasoning
# model = "claude-opus-4-20250514"               # Claude 4 Opus with reasoning
# model = "claude-3-7-sonnet-20250219"           # Claude 3.7 Sonnet

# Gemini Reasoning Models:
# model = "gemini/gemini-2.5-pro"                # Latest Gemini with reasoning
# model = "gemini/gemini-2.5-flash"              # Large text input with reasoning

# Perplexity Reasoning Models:
# model = "perplexity/sonar-reasoning-pro"       # Web access with reasoning capabilities

# Define a complex prompt that benefits from reasoning
# This type of question requires step-by-step thinking
prompt = """
Analyze this business scenario step by step:

A software company is deciding between two strategies:
1. Focus on enterprise clients (higher revenue per client, longer sales cycles)
2. Target small businesses (lower revenue per client, faster sales cycles)

They have a team of 10 salespeople and $500K marketing budget.
Current market: 1000 enterprises, 50,000 small businesses.
Enterprise conversion rate: 2%, avg deal: $100K
Small business conversion rate: 8%, avg deal: $5K

Which strategy should they choose and why? Show your reasoning process.
"""

# =============================================================================
# REQUEST PREPARATION
# =============================================================================

# Set up HTTP headers required for the API request
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

# Create the request payload with reasoning parameters
data = {
    "model": model,  # Which reasoning model to use
    "messages": [
        {"role": "user", "content": prompt}
    ],  # Complex question requiring reasoning
    "max_tokens": 2000,  # Higher token limit for detailed reasoning
    "temperature": 0.3,  # Lower temperature for more focused reasoning
    "stream": True,  # Enable streaming for real-time responses
    "reasoning_effort": "high",  # Enable maximum reasoning capability (low/medium/high)
}

# Construct the complete API URL
api_full = f"{api_endpoint}/chat/completions"

# =============================================================================
# API REQUEST EXECUTION
# =============================================================================

print("🧠 Reasoning Model Example")
print("=" * 50)
print(f"Model: {model}")
print(f"Reasoning Effort: {data['reasoning_effort']}")
print("=" * 50)

# Start animated thinking indicator
print()  # Add newline for clean animation
thinking_active = True
thinking_thread = threading.Thread(target=animate_thinking, daemon=True)
thinking_thread.start()

# Make the HTTP POST request with extended timeout for reasoning models
response = requests.post(api_full, headers=headers, json=data, stream=True, timeout=180)

# =============================================================================
# RESPONSE PROCESSING
# =============================================================================

if response.status_code == 200:

    # Track if we've started receiving content
    content_started = False

    # Process the streaming response
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
                    choice = data["choices"][0]

                    # Handle reasoning content
                    if "delta" in choice:
                        delta = choice["delta"]
                        if "content" in delta:
                            # Clear thinking indicator and show header on first content
                            if not content_started:
                                thinking_active = False  # Stop animation
                                time.sleep(0.1)  # Brief pause to let animation stop
                                print(
                                    "\r🤔 AI is thinking... Done!     "
                                )  # Clear line with completion
                                print("\n🧠 AI Reasoning Process (streaming):")
                                print("-" * 50)
                                content_started = True
                            print(delta["content"], end="", flush=True)

                    # Check for completion
                    if choice.get("finish_reason"):
                        print(f"\n\n✅ Reasoning completed: {choice['finish_reason']}")
                        break

            except json.JSONDecodeError:
                continue  # Skip malformed JSON

    # If no content was received, still show completion
    if not content_started:
        thinking_active = False  # Stop animation
        time.sleep(0.1)  # Brief pause to let animation stop
        print("\r🤔 AI is thinking... Complete!     ")  # Clear line
        print("\n🧠 AI Reasoning Process completed (no content received)")
        print("-" * 50)

    print("\n" + "-" * 50)
    print("🎯 Reasoning analysis completed.")

else:
    thinking_active = False  # Stop animation on error
    time.sleep(0.1)  # Brief pause to let animation stop
    print(f"\r❌ Request failed: {response.status_code}")
    print(f"Error details: {response.text}")

print("\n💡 Tip: Reasoning models work best with:")
print("   • Complex analytical questions")
print("   • Multi-step problem solving")
print("   • Logic puzzles and scenarios")
print("   • Strategic decision making")
