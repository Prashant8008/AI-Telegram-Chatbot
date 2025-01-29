import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_text(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = await model.generate_content_async(prompt)
    return response.text

async def analyze_image(image_url):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = await model.generate_content_async(f"Describe this image: {image_url}")
    return response.text