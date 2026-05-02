#trying to get nano banana to work in this file

from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import base64

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini OpenAI-compatible setup
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key=api_key
)

model = "gemini-2.5-flash-image" 

# UI
st.title("🍌 Nano Banana Image Generator")

prompt = st.text_input("Enter prompt", "A futuristic banana robot in space")

if st.button("Generate"):
    with st.spinner("Cooking pixels... 🍳"):
        response = client.images.generate(
            model=model,
            prompt=prompt
        )

        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        st.image(image_bytes, caption=prompt)
