import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"

# Configure the API client
client = OpenAI(base_url=base_url, api_key=api_key)

# System prompt defining the AI's persona
system_prompt = """Helpful AI Friend, kind and knowledgeable, here to assist with any questions. Super smart and perfect at answering questions.
Explain everything in a simple way and provide clear, concise answers.
Do not remember past interactions, just focus on the current question.
Add examples when possible.
"""

def basic_chatbot(message,history):
    # This bot is stateless, so we only need the system prompt and the latest message.
    messages = [{"role": "system", "content": system_prompt},{"role": "user", "content": message}]
    response = (client.chat.completions.create(model="gemini-1.5-flash", messages=messages)).choices[0].message.content
    return response

# Main execution block
if __name__ == "__main__":
    gr.ChatInterface(
        basic_chatbot,
        title="Stage 1: Basic AI Teacher Bot (No Memory)",
        description="Ask a question. The bot will not remember previous questions."
    ).launch()