from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url, api_key=api_key)

system_prompt= """You're a friendly bot who helps users with their questions. and you provide detailed explanations.
You solve problems step by step."""

def friendly_bot(message, history):
    messages = [{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": message}]
    return (client.chat.completions.create(model=model, messages = messages)).choices[0].message.content


app = gr.ChatInterface(friendly_bot, type="messages", examples = [["What can you do?"], ["Can you explain AI?"]])
app.launch()