import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Text to Image Generator (DALL-E)")
prompt = st.text_input("Enter a prompt to generate the image:")

if st.button("Generate Image"):
    if prompt:
        try:
            with st.spinner("Generating image..."):
                # Call OpenAI's DALL-E API to generate the image
                response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            st.image(image_url, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error generating image: {e}")
    else:
        st.error("Please enter a prompt to generate the image.")