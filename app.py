import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("DEEPSEEK_API_KEY")

# 2. Setup the Client
client = OpenAI(
    api_key=key,
    base_url="https://api.deepseek.com"
)

def completion(message, history):
    messages = []
    
    # Handle the old Gradio history format
    for interaction in history:
        if isinstance(interaction, (list, tuple)):
            user_msg, assistant_msg = interaction
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
        elif isinstance(interaction, dict):
            messages.append(interaction)

    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="deepseek-v4-pro"
    )
    return chat_completion.choices[0].message.content

demo = gr.ChatInterface(
    fn=completion,
    title="LEO-AI TUTOR",
    description="Ask me anything!"
)

if __name__ == "__main__":
    demo.launch()