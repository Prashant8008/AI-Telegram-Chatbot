import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def sentiment_analysis(text):
    """
    Analyzes the sentiment of a given text using Hugging Face's sentiment analysis model.

    Args:
    - text (str): The text for sentiment analysis.

    Returns:
    - tuple: A tuple containing the sentiment score and label.
    """
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Parse the response
    sentiment = response.json()
    
    if sentiment:
        label = sentiment[0]
        sentiment_score = label  # Hugging Face's model typically returns integer labels (0 to 4)
        return sentiment_score, label
    return None, None
