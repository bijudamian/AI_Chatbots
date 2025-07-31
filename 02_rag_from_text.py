from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import gradio as gr

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
client = OpenAI(base_url=base_url,api_key=api_key)

url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
response = requests.get(url)

file_path = "text.txt"
with open(file_path, "wb") as f:
    f.write(response.content)

try:
    with open(file_path, "r", encoding = "utf8") as d:
        text = d.readlines()
        text_context = "\n".join([line.strip() for line in text if line.strip()])
except Exception as e:
    print(f"Error is : {e}")

system_prompt = f"""You are Ragger, an AI assistant at HERE AND NOW AI - Artificial Intelligence Research Institute.
    Your mission is to **answer questions about HERE AND NOW AI** and its **prospectus**.
    use the following context to answer questions: {text_context}"""

def ragger(message,history):
    messages = [{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": message}]
    response = (client.chat.completions.create(model=model, messages=messages)).choices[0].message.content
    return response

app = gr.ChatInterface(ragger, type="messages", examples=[["What is HERE AND NOW AI?"],["Who is the CEO, CTO and CMO of HANA?"], ["Tell me about the prospectus."]])
app.launch()