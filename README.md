# Expedient AI API Examples

This repository contains examples and documentation for integrating with the Expedient AI Chat API. Our gateway provides access to multiple AI providers including OpenAI, Claude, Gemini, and Perplexity models through a unified private and secure interface.

## Quick Start

1. **Get your API key** from Expedient AI
2. **Create and activate a virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Update the API key** in the example file that you are running
5. **Run the examples:**
   ```bash
   # Quick test (simplest)
   python quick_start.py
   
   # Standard streaming models
   python example.py
   
   # Reasoning models (for complex analysis)
   python reasoning_example.py

   # Web access models with citations (for live web search)
   python citation_example.py
   
   # OR use cURL commands directly (see curl.md)
   curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
     -d '{"model": "gpt-4.1", "messages": [{"role": "user", "content": "Hello!"}]}'
   ```

## Files in this Repository

### 📄 `quick_start.py`
Minimal example for immediate testing. Features:
- Ultra-simple code (30 lines)
- No comments or explanations
- Just the essentials for quick API testing
- Perfect for copy-paste and quick modifications

### 📄 `example.py`
Complete Python script demonstrating streaming AI responses with standard models. Features:
- Real-time streaming responses
- Standard AI models (GPT, Claude, Gemini, Perplexity)
- Detailed comments and explanations
- Production-ready streaming implementation

### 📄 `reasoning_example.py`
Advanced reasoning models with animated thinking indicators. Features:
- Complex analytical problem solving
- Step-by-step reasoning processes
- Animated thinking dots while processing
- Models: o4-mini, o3, Claude 4, Gemini 2.5

### 📄 `citation_example.py`
Perplexity web reasoning models with real-time data and citations. Features:
- Real-time web search during AI responses
- Current events and fact-checking capabilities
- Automatic citation detection and reporting
- Animated search indicators

### 📄 `postman.md`
Complete Postman collection documentation with:
- 8 ready-to-use API request examples
- All supported AI models and providers
- Parameter explanations and usage tips
- Import instructions for Postman

### 📄 `curl.md`
Command-line cURL examples for developers and scripters. Features:
- 8 cURL commands matching all Postman examples
- Advanced options and streaming processing
- Environment variable setup for security
- Batch processing and error handling examples

### 📄 `.gitignore`
Python-specific gitignore file that excludes:
- Virtual environments
- API keys and sensitive files
- Python cache files
- IDE configuration files

## Supported AI Providers

Our unified API gateway supports models from:

- **OpenAI:** GPT-4.1 (default), o4-mini (reasoning), GPT-4o, GPT-4o-mini, GPT-3.5-turbo
- **Anthropic:** Claude-4-Sonnet (reasoning), Claude-3.7-Sonnet, Claude-3.5-Sonnet, Claude-3-Haiku, Claude-3-Opus
- **Google:** Gemini-2.5-Pro (reasoning), Gemini-2.5-Flash (reasoning), Gemini-1.5-Pro, Gemini-1.5-Flash
- **Perplexity:** Sonar-Pro, Sonar-Reasoning-Pro, Sonar (all web-connected with real-time data)

## Key Features

✅ **Unified Interface** - One API for multiple AI providers  
✅ **Real-time Streaming** - See responses as they're generated  
✅ **Multiple Models** - Choose the best model for your use case  
✅ **Web Access & Citations** - Real-time data with source transparency  
✅ **Quick Start** - Ultra-simple 30-line example for immediate testing  
✅ **Enterprise Ready** - Production-grade error handling  
✅ **Easy Integration** - Simple REST API with JSON  

## API Endpoint

```
[ ENTER_CHAT_URL_HERE ]/chat/completions
```

## Authentication

All requests require a Bearer token in the Authorization header:

```
Authorization: Bearer [ ENTER_API_KEY_HERE ]
```

## Basic Usage Example

```python
import requests
import json

# Simple streaming request
response = requests.post(
    "[ ENTER_CHAT_URL_HERE ]/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer [ ENTER_API_KEY_HERE ]"
    },
    json={
        "model": "gpt-4.1",
        "messages": [{"role": "user", "content": "Hello, world!"}],
        "stream": True
    },
    stream=True
)

# Process streaming response
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
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- Valid Expedient AI API key

### Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy your API key from the Expedient AI dashboard
5. Update the `api_key` variable in the script you want to use
6. Run the examples:
   ```bash
   # Quick test
   python quick_start.py
   
   # Standard streaming models  
   python example.py
   
   # Reasoning models
   python reasoning_example.py
   
   # Web search with citations
   python citation_example.py
   ```

## Model Selection Guide

Choose the right model for your needs:

| Use Case | Recommended Models |
|----------|-------------------|
| **Advanced Reasoning & Logic** | `o4-mini`, `claude-sonnet-4-20250514`, `gemini/gemini-2.5-pro` |
| **Complex Analysis** | `gpt-4.1`, `gpt-4o`, `claude-3-7-sonnet-20250219`, `gemini/gemini-1.5-pro` |
| **Large Text Processing** | `gemini/gemini-2.5-flash` (1M+ token context) |
| **Creative Writing** | `claude-sonnet-4-20250514`, `claude-3-7-sonnet-20250219`, `gpt-4o` |
| **Code Generation** | `gpt-4.1`, `claude-sonnet-4-20250514`, `gpt-4o` |
| **Fast Responses** | `gpt-4o-mini`, `claude-3-haiku-20240307`, `gemini/gemini-1.5-flash` |
| **Current Events & Web Data** | `perplexity/sonar-reasoning-pro`, `perplexity/sonar-pro` |
| **General Purpose** | `gpt-4.1` (default), `gpt-3.5-turbo` |

## Documentation

- **[Postman Collection](postman.md)** - Complete API testing examples
- **[cURL Examples](curl.md)** - Command-line examples for terminal and scripts
- **[Quick Start](quick_start.py)** - Minimal example for immediate testing
- **[Standard Streaming Example](example.py)** - Detailed implementation with comments
- **[Reasoning Example](reasoning_example.py)** - Advanced reasoning with thinking animation
- **[Citation Example](citation_example.py)** - Web search with real-time citations
- **API Documentation** - Contact Expedient AI for detailed API docs

## Support

For technical support and API access:
- **Website:** [Expedient AI](https://expedient.cloud)
- **Documentation:** See `postman.md` for comprehensive examples
- **Issues:** Use this repository's issue tracker for code-related questions

## Security Notes

🔒 **Never commit API keys to version control**  
🔒 **Use environment variables for production deployments**  
🔒 **Rotate API keys regularly**  
🔒 **Monitor API usage and costs**

## License

This example code is provided for demonstration purposes. Please check with Expedient AI for licensing terms for the API service itself. 