import gradio as gr
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable not set")

# Model to use
MODEL = "meta-llama/llama-4-maverick:free"

def chat_with_openrouter(message, history):
    # Prepare the conversation history in the format expected by the API
    messages = []

    messages.append({
        "role": "system",
        "content": "You are helpful assistant that can answer questions and help with tasks."
    })
    
    # Add conversation history
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    # Add the new message
    messages.append({"role": "user", "content": message})
    
    # Make the API request
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": MODEL,
            "messages": messages
        })
    )
    
    # Parse the response
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_with_openrouter,
    title="Chat with Llama-4-maverick via OpenRouter",
    description="This is a simple chat interface using OpenRouter API with the meta-llama/llama-4-maverick:free model.",
    examples=["Hello, how are you?", "What can you tell me about artificial intelligence?", "Write a short poem about nature."],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch() 