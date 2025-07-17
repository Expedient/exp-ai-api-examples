# Expedient AI API - cURL Examples

This document provides comprehensive cURL command examples for the Expedient AI Chat API. These commands can be run directly from your terminal or integrated into scripts and applications.

## Base Configuration

**Base URL:** `[ ENTER_CHAT_URL_HERE ]`  
**Endpoint:** `/chat/completions`  
**Authentication:** Bearer Token (API Key)

## cURL Examples

### 1. Non-Streaming Request

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      {
        "role": "user",
        "content": "Explain the benefits of AI in business."
      }
    ],
    "max_tokens": 256,
    "temperature": 0.7,
    "stream": false
  }'
```

### 2. Streaming Request

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      {
        "role": "user",
        "content": "Write a detailed analysis of cloud computing trends."
      }
    ],
    "max_tokens": 500,
    "temperature": 0.7,
    "stream": true
  }'
```

### 3. Multi-Message Conversation

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful AI assistant specializing in enterprise technology."
      },
      {
        "role": "user",
        "content": "What are the main challenges in AI implementation?"
      },
      {
        "role": "assistant",
        "content": "The main challenges include data quality, integration complexity, and skill gaps."
      },
      {
        "role": "user",
        "content": "How can organizations overcome these challenges?"
      }
    ],
    "max_tokens": 300,
    "temperature": 0.6,
    "stream": true
  }'
```

### 4. Claude Model Example

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [
      {
        "role": "user",
        "content": "Analyze the pros and cons of hybrid cloud architecture for enterprise applications."
      }
    ],
    "max_tokens": 500,
    "temperature": 0.5,
    "stream": true
  }'
```

### 5. Gemini Model Example

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "gemini/gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": "Create a technical roadmap for implementing AI in a manufacturing environment."
      }
    ],
    "max_tokens": 600,
    "temperature": 0.3,
    "stream": true
  }'
```

### 6. Perplexity Model Example (Web-Connected)

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "perplexity/sonar-pro",
    "messages": [
      {
        "role": "user",
        "content": "What are the latest developments in AI regulations and compliance requirements?"
      }
    ],
    "max_tokens": 400,
    "temperature": 0.4,
    "stream": true
  }'
```

### 7. Reasoning Model Example (o4-mini)

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "o4-mini",
    "messages": [
      {
        "role": "user",
        "content": "Solve this logic puzzle step by step: If all cats are animals, and some animals are pets, what can we conclude about cats and pets?"
      }
    ],
    "max_tokens": 600,
    "temperature": 0.3,
    "reasoning_effort": "high",
    "stream": true
  }'
```

### 8. Web Reasoning Example (Perplexity with Citations)

```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{
    "model": "perplexity/sonar-reasoning-pro",
    "messages": [
      {
        "role": "user",
        "content": "What are the latest developments in AI regulation in 2025? Analyze the potential impact on enterprise adoption and provide specific examples with sources."
      }
    ],
    "max_tokens": 1500,
    "temperature": 0.4,
    "stream": true
  }'
```

**Note:** This model provides real-time web search with citations embedded in the response as [1], [2], etc.

## Supported AI Models

### OpenAI Models
- `gpt-4.1` - Latest general AI model (default)
- `o4-mini` - Advanced reasoning model with enhanced logic
- `gpt-4o` - Latest GPT-4 model, best for complex reasoning
- `gpt-4o-mini` - Faster, cost-effective version of GPT-4
- `gpt-3.5-turbo` - Fast and efficient for most tasks

### Claude Models (Anthropic)
- `claude-sonnet-4-20250514` - Latest Claude 4 Sonnet with reasoning capabilities
- `claude-3-7-sonnet-20250219` - Claude 3.7 Sonnet
- `claude-3-5-sonnet-20241022` - Claude 3.5 Sonnet (proven performance)
- `claude-3-haiku-20240307` - Fast and efficient Claude model
- `claude-3-opus-20240229` - Most capable Claude 3 model for complex tasks

### Gemini Models (Google)
- `gemini/gemini-2.5-pro` - Latest Gemini with reasoning capabilities
- `gemini/gemini-2.5-flash` - Large text input with reasoning capabilities
- `gemini/gemini-1.5-pro` - Google's proven model for complex reasoning
- `gemini/gemini-1.5-flash` - Faster Gemini model for quick responses

### Perplexity Models (Web-Connected)
- `perplexity/sonar-pro` - Web access with enhanced capabilities
- `perplexity/sonar-reasoning-pro` - Web access with reasoning capabilities
- `perplexity/sonar` - Standard web-connected model with real-time data

## Model Selection Guide

Choose the right model based on your use case:

- **For ADVANCED REASONING & LOGIC:** o4-mini, claude-sonnet-4-20250514, gemini/gemini-2.5-pro
- **For COMPLEX ANALYSIS:** gpt-4.1, gpt-4o, claude-3-7-sonnet-20250219, gemini/gemini-1.5-pro
- **For LARGE TEXT PROCESSING:** gemini/gemini-2.5-flash (1M+ token context)
- **For CREATIVE WRITING:** claude-sonnet-4-20250514, claude-3-7-sonnet-20250219, gpt-4o
- **For CODE GENERATION:** gpt-4.1, claude-sonnet-4-20250514, gpt-4o
- **For FAST RESPONSES & COST EFFICIENCY:** gpt-4o-mini, claude-3-haiku-20240307, gemini/gemini-1.5-flash
- **For CURRENT EVENTS & WEB DATA:** perplexity/sonar-reasoning-pro (with citations), perplexity/sonar-pro
- **For GENERAL PURPOSE:** gpt-4.1 (default), gpt-3.5-turbo

## Available Parameters

- **model:** AI model to use (see supported models above)
- **messages:** Array of conversation messages with role and content
- **max_tokens:** Maximum tokens in response (1-4096)
- **temperature:** Creativity level (0.0-2.0, where 0 is deterministic)
- **stream:** Boolean - enables real-time streaming responses
- **reasoning_effort:** For reasoning models (o4-mini, etc.) - options: "low", "medium", "high"
- **top_p:** Alternative to temperature (0.0-1.0)
- **frequency_penalty:** Reduces repetition (-2.0 to 2.0)
- **presence_penalty:** Encourages new topics (-2.0 to 2.0)

## cURL Tips for Testing

### Basic Setup
- Replace `[ ENTER_API_KEY_HERE ]` with your actual API key
- Replace `[ ENTER_CHAT_URL_HERE ]` with your actual chat URL
- Add `--no-buffer` for streaming responses to see real-time output

### Advanced Options
```bash
# Save response to file
curl ... > response.txt

# Include response headers
curl ... -i

# Verbose output for debugging
curl ... -v

# Set timeout (in seconds)
curl ... --max-time 120

# Follow redirects
curl ... -L

# Pretty print JSON response (requires jq)
curl ... | jq .
```

### Streaming Response Processing
For streaming responses, you can process the data in real-time:

```bash
# Stream and process with jq
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  --no-buffer \
  -d '{"model": "gpt-4.1", "messages": [{"role": "user", "content": "Hello"}], "stream": true}' \
  | while IFS= read -r line; do
      if [[ $line == data:* ]]; then
        echo "$line" | sed 's/^data: //' | jq -r '.choices[0].delta.content // empty'
      fi
    done
```

### Error Handling
```bash
# Check HTTP status code
response=$(curl -s -w "%{http_code}" -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  -d '{"model": "gpt-4.1", "messages": [{"role": "user", "content": "Hello"}]}')

http_code="${response: -3}"
response_body="${response%???}"

if [ "$http_code" -eq 200 ]; then
  echo "Success: $response_body"
else
  echo "Error $http_code: $response_body"
fi
```

## Environment Variables
For security and convenience, use environment variables:

```bash
# Set environment variables
export EXPEDIENT_API_KEY="your-api-key-here"
export EXPEDIENT_API_URL="your-api-url-here"

# Use in curl commands
curl -X POST "$EXPEDIENT_API_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXPEDIENT_API_KEY" \
  -d '{"model": "gpt-4.1", "messages": [{"role": "user", "content": "Hello"}], "stream": true}'
```

## Common Use Cases

### Quick API Test
```bash
curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
  -d '{"model": "gpt-4.1", "messages": [{"role": "user", "content": "Say hello"}]}'
```

### Batch Processing
```bash
# Process multiple prompts
prompts=("Explain AI" "What is ML?" "Define cloud computing")
for prompt in "${prompts[@]}"; do
  echo "Processing: $prompt"
  curl -X POST "[ ENTER_CHAT_URL_HERE ]/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer [ ENTER_API_KEY_HERE ]" \
    -d "{\"model\": \"gpt-4.1\", \"messages\": [{\"role\": \"user\", \"content\": \"$prompt\"}]}" \
    | jq -r '.choices[0].message.content'
  echo "---"
done
``` 