import gradio as gr
import requests
import json
import os
from dotenv import load_dotenv
from typing import Dict, Any, List

# LlamaIndex imports
from llama_index.llms.openrouter import OpenRouter
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

# Load environment variables
load_dotenv()

# Get API key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable not set")

# Model to use
MODEL = "meta-llama/llama-4-maverick:free"

def get_crypto_price(crypto: str, currency: str = "usd") -> str:
    """Fetches the real-time price of a cryptocurrency using CoinGecko.
    Args:
        crypto: The name of the cryptocurrency (e.g., 'bitcoin').
        currency: The fiat currency to convert the price into (default: 'usd').
    Returns:
        A string with the real-time price.
    """
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto.lower()}&vs_currencies={currency.lower()}"
        response = requests.get(url)
        data = response.json()

        if crypto.lower() not in data:
            return f"⚠️ Cryptocurrency '{crypto}' not found."

        price = data[crypto.lower()][currency.lower()]
        return f"💰 Current price of {crypto.capitalize()}: {price} {currency.upper()}"
    
    except Exception as e:
        return f"❌ Error fetching price: {str(e)}"

# Initialize OpenRouter LLM
def init_llm():
    llm = OpenRouter(
        model=MODEL,
        api_key=OPENROUTER_API_KEY
    )
    return llm

# Initialize tools
def init_tools():
    crypto_price_tool = FunctionTool.from_defaults(
        name="get_crypto_price",
        fn=get_crypto_price,
        description="Get the current price of a cryptocurrency in a specified currency"
    )
    return [crypto_price_tool]

# Initialize ReAct agent
def init_agent():
    llm = init_llm()
    tools = init_tools()
    agent = ReActAgent.from_tools(
        tools=tools,
        llm=llm,
        verbose=True
    )
    # --- Add personality without overwriting core instructions ---

    # 1. Get the default prompts
    prompt_dict = agent.get_prompts()
    default_system_prompt_tmpl = prompt_dict.get("agent_worker:system_prompt", None)
    if default_system_prompt_tmpl:
        # 2. Define your custom personality/instructions
        custom_personality = """
        You are CryptoBot, a friendly and slightly enthusiastic assistant specializing in cryptocurrency prices.
        Always be helpful and provide clear price information using your tools.
        Remember to stay positive!
        Do not provide financial advice, just the facts with a smile!
        --- (Existing instructions below) ---
        """
        # 3. Get the default template string
        default_template_str = default_system_prompt_tmpl.template

        # 4. Prepend your personality to the default template
        new_template_str = custom_personality + "\n" + default_template_str

        # 5. Create a new PromptTemplate
        updated_system_prompt = PromptTemplate(new_template_str)

        # 6. Update the agent's prompts
        agent.update_prompts({"agent_worker:system_prompt": updated_system_prompt})
        print("✅ Successfully updated agent system prompt with personality.") # Optional: confirmation
    else:
        print("⚠️ Could not retrieve default system prompt to modify.") # Optional: error handling

    return agent

agent = init_agent()

def chat_with_agent(message, history):
    # Convert chat history to context
    context = ""
    if history:
        for human, assistant in history:
            context += f"Human: {human}\nAssistant: {assistant}\n"
    
    # Add current message to context
    if context:
        prompt = f"{context}Human: {message}\nAssistant:"
    else:
        prompt = f"Human: {message}\nAssistant:"
    
    # Query the agent
    try:
        response = agent.query(message)
        return response.response
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_with_agent,
    title="Agentic Solution with Llama-4-maverick via OpenRouter",
    description="This is a simple chat interface using OpenRouter API with the meta-llama/llama-4-maverick:free model. Try asking about cryptocurrency prices!",
    examples=[ 
        "What's the current price of bitcoin?",
        "What's the price of Doge?",
        "Compare the price of ethereum and solana",
        "create a table with the top crypto prices"
    ],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch() 