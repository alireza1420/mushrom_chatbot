"""A mushroom expert chatbot that responds to user queries about mushrooms.
"""
from google import genai
import os
import glob
import gradio as gr
import random
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def response(message, history,image):
    contents = []


    if message:
        contents.append(message)

    if image:  # if user uploads an image
        with open(image, "rb") as f:
            image_bytes = f.read()
        contents.append(
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg"
            )
        )


    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=contents,
    )
    return response.text
    
with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.ChatInterface(
        fn=response,
        additional_inputs=[gr.Image(type="filepath", label="Upload a Mushroom Image")],
        title="🍄 Multimodal Mushroom Expert 🍄",
        description="Ask questions about mushrooms or upload an image for analysis."
    )

if __name__ == "__main__":
    demo.launch()
