import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def test():
    model = genai.GenerativeModel('gemini-pro')
    response = await model.generate_content_async("What is the capital of India?")
    print(response.text)

import asyncio
asyncio.run(test())
