import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
import PyPDF2
import gradio as gr

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
client = OpenAI(base_url=base_url, api_key=api_key)

url = "https://raw.githubusercontent.com/hereandnowai/sathyabama-be-cse-ai-pt1-07-2025-hands-on-professional-training-on-genai-and-ai-agents/main/general-profile-of-hereandnowai.pdf"
response = requests.get(url)

PDF_FILE_NAME = "prospectus.pdf"
PDF_DIR = os.path.dirname(__file__)
PDF_PATH = os.path.join(PDF_DIR, PDF_FILE_NAME)

with open(PDF_PATH, "wb") as f:
    f.write(response.content)

try:
    with open(PDF_PATH, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        # Extract text from each page
        pdf_text_chunks = []
        for page in reader.pages:
            pdf_text = page.extract_text()
            if pdf_text:
                pdf_text_chunks.append(pdf_text.strip())
        pdf_context = "\n".join(pdf_text_chunks) if pdf_text_chunks else "No text found in PDF."
except Exception as e:
    print(f"Error reading PDF: {e}")
    pdf_context = "Error reading PDF."

system_prompt = f"""context from {PDF_PATH}:{pdf_context}
You are RdfRagger, an AI assistant at HERE AND NOW AI - Artificial Intelligence Research Institute."""

def pdfragger(message, history):
    messages = [{"role": "system", "content": system_prompt}, *history, {"role": "user", "content": message}]
    response = (client.chat.completions.create(model=model, messages=messages)).choices[0].message.content
    return response

(gr.ChatInterface(pdfragger, type="messages")).launch()
