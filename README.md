# OpenRouter Chat Applications with Llama 4 Maverick

This repository contains two separate Gradio applications that demonstrate different ways to interact with the Llama 4 Maverick model via OpenRouter API:

1. **LLM Chat** - A simple chat interface for direct interaction with the LLM
2. **Agents Chat** - An enhanced chat interface with LlamaIndex ReAct agent capabilities and custom tools

## Features

**LLM Chat Application:**
- Basic chat interface with Llama 4 Maverick model
- Direct communication with OpenRouter API
- Conversation history maintained during the session

**Agents Chat Application:**
- Enhanced chat interface with LlamaIndex ReAct agent
- Tool integration for retrieving real-time cryptocurrency prices
- Advanced reasoning capabilities to handle complex tasks
- Full conversation history support

## Setup

1. Clone this repository
2. Install the requirements (shared by both applications):
   ```
   pip install -r requirements.txt
   ```
3. Create `.env` files in both directories from their respective examples:
   ```
   cp LLM/.env.example LLM/.env
   cp Agents/.env.example Agents/.env
   ```
4. Add your OpenRouter API key to both `.env` files:
   ```
   OPENROUTER_API_KEY=your_actual_api_key
   ```

## Usage

### Running the Simple LLM Chat

```
python LLM/main.py
```

This will start a basic chat interface with the Llama 4 Maverick model. The application provides a straightforward way to interact with the model for general conversation and information retrieval.

### Running the Agents Chat

```
python Agents/main.py
```

This will start the enhanced version of the chat interface that incorporates the LlamaIndex ReAct agent. This version includes tools like cryptocurrency price checking and demonstrates how agents can perform reasoning over multiple steps to accomplish tasks.

Both applications will start a local Gradio server, typically at http://127.0.0.1:7860

## Example Queries

**For LLM Chat:**
- "Hello, how are you?"
- "What can you tell me about artificial intelligence?"
- "Write a short poem about nature."

**For Agents Chat:**
- "What's the current price of bitcoin?"
- "Compare the price of ethereum and solana"
- "Is bitcoin more expensive than ethereum right now?"
- "Which cryptocurrency has grown the most in the last 24 hours?"

## Requirements

- Python 3.10 or higher
- An OpenRouter API key
- Active internet connection to communicate with the OpenRouter API
- For the Agents version, internet access to the CoinGecko API for cryptocurrency data

## Workshop Steps

Follow these steps to get hands-on experience with the LLM and Agents applications:

1. **Create a Python Virtual Environment**

   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup OpenRouter API Key**
   - Get your API key from [OpenRouter](https://openrouter.ai/)
   - Copy `LLM/.env.example` to `LLM/.env`
   - Add your API key to the `.env` file:
     ```
     OPENROUTER_API_KEY=your_actual_api_key
     ```

4. **Run the Basic LLM Chat**
   ```bash
   cd LLM
   python main.py
   ```
   - Open the Gradio UI URL (typically http://127.0.0.1:7860)
   - Test the basic chat functionality

5. **Customize System Prompt**
   - Open `LLM/main.py`
   - Locate the system prompt section
   - Modify it to see how it affects the model's behavior
   - Example benefits of customizing system prompts:
     - Control the model's personality and tone
     - Set specific constraints or guidelines
     - Define the model's role and expertise
     - Improve response quality and relevance

6. **Explore the Agents Version**
   ```bash
   cd ../Agents
   python main.py
   ```
   - Observe how the agent can access cryptocurrency price data
   - Test queries like "What's the current price of bitcoin?"

7. **Add Custom Tools**
   - Navigate to the `tools` folder
   - Examine `get_weather.py` or `search_news.py`
   - These files demonstrate how to create tools that call external APIs
   - To add a new tool:
     1. Copy the tool function from `tools/get_weather.py` or `search_news.py`
     2. Add it to `Agents/main.py`
     3. Update the ReActAgent configuration to include the new tool
     4. Restart the application to test the new functionality

This workshop demonstrates how to:
- Set up and run LLM applications
- Customize model behavior through system prompts
- Extend LLM capabilities with custom tools
- Integrate external APIs into your applications