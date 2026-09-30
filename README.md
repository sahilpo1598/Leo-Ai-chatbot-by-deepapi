Here is an upgraded, professional version of your `README.md`. It fixes the syntax errors in your code blocks, updates the cloned URL to match your repository name, and adds clear sections for prerequisites, environment setup, usage, and project structure.

---

# Leo — DeepSeek AI Chatbot

A simple, fast, and conversational AI chatbot interface powered by the **DeepSeek API** and built with **Gradio** and **Python**.

---

## Features

* **Interactive UI:** Clean, intuitive web interface provided by Gradio.
* **DeepSeek Integration:** Powered by DeepSeek's language models for fast and intelligent responses.
* **Secure Configuration:** Environment variables managed securely using `.env` files to keep API credentials safe.

---

## Tech Stack

* **Language:** Python 3.10+
* **Framework:** Gradio
* **API:** DeepSeek API
* **Environment Management:** python-dotenv

---

## Project Structure

```text
Leo-Ai-chatbot-by-deepapi/
├── app.py              # Main application script
├── .env                # Local API keys (Git-ignored)
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

```

---

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine and an active API key from the [DeepSeek Platform](https://platform.deepseek.com/).

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/sahilpo1598/Leo-Ai-chatbot-by-deepapi.git
cd Leo-Ai-chatbot-by-deepapi

```


2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

```


3. **Install the dependencies:**
```bash
pip install -r requirements.txt

```


4. **Set up environment variables:**
Create a `.env` file in the root directory and add your DeepSeek API key:
```env
DEEPSEEK_API_KEY=your_actual_deepseek_api_key_here

```



---

## Usage

Run the main application script:

```bash
python app.py

```

Once the script starts, Gradio will generate a local URL (typically `[http://127.0.0.1:7860](http://127.0.0.1:7860)`). Open that link in your browser to start chatting with Leo.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.