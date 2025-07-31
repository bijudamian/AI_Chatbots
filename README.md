# Progressive AI Chatbot Development

This repository demonstrates the step-by-step evolution of an AI chatbot. Starting from a basic, stateless agent, the project progressively adds features like conversational memory and Retrieval-Augmented Generation (RAG) from both text and PDF files.

The project uses Python with the Gemini API (via an OpenAI-compatible wrapper) and Gradio for a user-friendly web interface.

## The 4 Stages of Development

Each script represents a clear step in the development process:

1.  **`00_Basic_Chatbot.py`**
    * **Feature:** A foundational, stateless chatbot.
    * **Description:** This is the simplest version. It answers each question independently and does not remember any previous part of the conversation.

2.  **`01_Chatbot_with_history.py`**
    * **Feature:** Conversational Memory.
    * **Description:** This stage enhances the bot by adding memory. It takes the previous conversation history into account to provide more relevant and contextual responses.

3.  **`02_rag_from_text.py`**
    * **Feature:** Retrieval-Augmented Generation (RAG) from a Text File.
    * **Description:** The bot's capabilities are extended with RAG. It fetches data from an external `.txt` file from a URL to answer questions factually based on the provided document.

4.  **`03_rag_from_pdf.py`**
    * **Feature:** Advanced RAG from a PDF File.
    * [cite_start]**Description:** The final stage demonstrates a more powerful RAG system that can download a PDF document, extract its text content, and use that information to answer user questions[cite: 1].

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites
* Python 3.7+
* A Gemini API Key

### Step 1: Clone the Repository
```bash
git clone https://github.com/bijudamian/AI_Chatbots.git
cd AI_Chatbots
```

### Step 2: Create a Virtual Environment (Recommended)
It's best practice to create a virtual environment to manage project dependencies.

```Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Dependencies
Install all the required Python libraries from the requirements.txt file.

```Bash

pip install -r requirements.txt
```
### Step 4: Configure Your API Key
You need to create a .env file to securely store your API key.
```bash
Create a file named .env in the root directory of the project.

Open the .env file and add your Gemini API key in the following format:

GEMINI_API_KEY="AIza....."
```

## 🚀 How to Run Each Stage
You can run each script individually to see the chatbot's evolution. After running a command, a local URL (e.g., http://127.0.0.1:7860) will appear in your terminal. Open this URL in your web browser to interact with the bot.

### Run the Basic Chatbot:

```Bash

python 00_Basic_Chatbot.py

```
### Run the Chatbot with History:
```Bash

python 01_Chatbot_with_history.py

```
### Run the RAG Bot (from Text):
```Bash

python 02_rag_from_text.py

```
### Run the RAG Bot (from PDF):
```Bash

python 03_rag_from_pdf.py
```
