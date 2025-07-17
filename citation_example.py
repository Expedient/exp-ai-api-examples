"""
Perplexity Web Reasoning Example - Python Client
================================================

This script demonstrates how to use Perplexity's reasoning models with web access.
These models can search the web in real-time and provide citations for their answers,
making them perfect for current events, research, and fact-checking.

NOTE: Your AI account must have web access models enabled.

For complete API documentation see postman.md
For standard models see example.py
"""

# Import required libraries for HTTP requests and JSON processing
import requests  # For making HTTP API calls
import json  # For parsing JSON data from streaming responses
import re  # For processing citations
import threading  # For animated thinking dots
import time  # For timing the dot animation

# =============================================================================
# ANIMATED THINKING INDICATOR
# =============================================================================


def animate_thinking():
    """Show animated dots while AI is searching and thinking"""
    dots = [".", "..", "..."]
    i = 0
    while thinking_active:
        print(f"\r🔍 Searching web and thinking{dots[i % 3]}   ", end="", flush=True)
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

# Perplexity Web Reasoning Models
# These models search the web and provide citations

model = "perplexity/sonar-reasoning-pro"  # Web access with reasoning (recommended)

# Alternative web reasoning model:
# model = "perplexity/sonar-reasoning"     # Standard web reasoning model

# Define prompts that benefit from real-time web data and reasoning
# These questions require current information and analysis
prompts = [
    "What are the latest developments in AI regulation in 2025? Analyze the potential impact on enterprise adoption.",
    "Compare the current market performance of major cloud providers (AWS, Azure, GCP) in Q4 2024 and explain the trends.",
    "What are the most recent cybersecurity threats businesses should be aware of? Provide specific examples and mitigation strategies.",
    "Analyze the latest trends in remote work technology and their impact on enterprise productivity in 2025.",
]

# Select which prompt to use (0-3)
selected_prompt = 0
prompt = prompts[selected_prompt]

# =============================================================================
# REQUEST PREPARATION
# =============================================================================

# Set up HTTP headers required for the API request
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

# Create the request payload optimized for web reasoning
data = {
    "model": model,  # Perplexity reasoning model with web access
    "messages": [
        {"role": "user", "content": prompt}
    ],  # Question requiring current web data
    "max_tokens": 1500,  # Higher limit for detailed analysis with citations
    "temperature": 0.4,  # Balanced temperature for factual yet analytical responses
    "stream": True,  # Enable streaming for real-time responses
}

# Construct the complete API URL
api_full = f"{api_endpoint}/chat/completions"

# =============================================================================
# API REQUEST EXECUTION
# =============================================================================

print("🌐 Perplexity Web Reasoning Example")
print("=" * 60)
print(f"Model: {model}")
print(f"Capabilities: Web Access + Reasoning + Citations")
print("=" * 60)
print(f"\n📋 Query: {prompt}")
print("\n" + "=" * 60)

# Start animated thinking indicator for web search + reasoning
print()  # Add newline for clean animation
thinking_active = True
thinking_thread = threading.Thread(target=animate_thinking, daemon=True)
thinking_thread.start()

# Make the HTTP POST request with extended timeout for web search + reasoning
response = requests.post(api_full, headers=headers, json=data, stream=True, timeout=120)

# =============================================================================
# RESPONSE PROCESSING WITH CITATION HANDLING
# =============================================================================

if response.status_code == 200:
    full_response = ""  # Store complete response for citation processing
    content_started = False  # Track if we've started receiving content

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

                    # Handle streaming content
                    if "delta" in choice:
                        delta = choice["delta"]
                        if "content" in delta:
                            # Clear thinking indicator and show header on first content
                            if not content_started:
                                thinking_active = False  # Stop animation
                                time.sleep(0.1)  # Brief pause to let animation stop
                                print(
                                    "\r🔍 Searching web and thinking... Found sources!     "
                                )  # Clear line
                                print("\n🔍 Web Search + Reasoning (streaming):")
                                print("-" * 60)
                                content_started = True

                            content = delta["content"]
                            print(content, end="", flush=True)
                            full_response += content

                    # Check for completion with citations
                    if choice.get("finish_reason"):
                        break

            except json.JSONDecodeError:
                continue  # Skip malformed JSON

    # If no content was received, still show completion
    if not content_started:
        thinking_active = False  # Stop animation
        time.sleep(0.1)  # Brief pause to let animation stop
        print("\r🔍 Searching web and thinking... Complete!     ")  # Clear line
        print("\n🔍 Web Search + Reasoning completed (no content received)")
        print("-" * 60)

    # Process and display citations if present
    print("\n\n" + "=" * 60)
    print("📚 SOURCES & CITATIONS")
    print("=" * 60)

    # Look for citation patterns in the response
    citations = re.findall(r"\[(\d+)\]", full_response)
    if citations:
        print(f"✅ Found {len(set(citations))} citation(s) in the response")
        print("\n💡 Citations are embedded in the text above as [1], [2], etc.")
        print("   These refer to web sources the AI accessed during research.")
    else:
        print(
            "ℹ️  No explicit citations found, but response is based on current web data"
        )

    print("\n" + "=" * 60)
    print("🎯 Web reasoning analysis completed.")

else:
    thinking_active = False  # Stop animation on error
    time.sleep(0.1)  # Brief pause to let animation stop
    print(f"\r❌ Request failed: {response.status_code}")
    print(f"Error details: {response.text}")
    if response.status_code == 403:
        print("\n💡 Note: Web access models may require special account permissions")

print("\n" + "=" * 60)
print("💡 ABOUT PERPLEXITY WEB REASONING:")
print("=" * 60)
print("✅ Real-time web search during response generation")
print("✅ Reasoning through complex, current information")
print("✅ Built-in citation system for source transparency")
print("✅ Perfect for current events, research, and fact-checking")
print("\n🔄 Try different prompts by changing 'selected_prompt' (0-3)")

print("\n" + "=" * 60)
print("📋 OTHER EXAMPLE QUERIES:")
print("=" * 60)
for i, example_prompt in enumerate(prompts):
    marker = "👉" if i == selected_prompt else "  "
    print(f"{marker} {i}: {example_prompt}")
