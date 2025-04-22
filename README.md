# OpenRouter Chat with Qwen 2.5 7B

A simple Gradio UI for chatting with the Qwen 2.5 7B model via OpenRouter API.

## Setup

1. Clone this repository
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file from the example:
   ```
   cp .env.example .env
   ```
4. Add your OpenRouter API key to the `.env` file
   ```
   OPENROUTER_API_KEY=your_actual_api_key
   ```

## Usage

Run the application:

```
python main.py
```

This will start a local Gradio server, typically at http://127.0.0.1:7860

You can now interact with the chat interface in your web browser.

## Features

- Simple chat interface with Qwen 2.5 7B model
- Conversation history is maintained during the session
- Example prompts provided

## Note

This application requires an active internet connection to communicate with the OpenRouter API.