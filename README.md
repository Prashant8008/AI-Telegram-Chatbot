# Telegram AI Chatbot with Gemini API Integration

This project is a Telegram bot powered by AI. The bot performs various tasks like user registration, handling user queries with AI-generated responses, analyzing images and files, and providing web search functionality. The chatbot is integrated with the Gemini API, which powers text generation and image analysis.

## Features

1. **User Registration**:
   - Saves user's name, username, chat ID, and phone number.
   - Uses Telegram's contact button for phone number collection.

2. **Gemini-Powered Chat**:
   - Uses the Gemini API to generate text responses based on user input.
   - Stores user inputs and bot responses in MongoDB with timestamps.

3. **Image/File Analysis**:
   - Accepts image files (JPG, PNG, PDF) and uses the Gemini API to describe the content of the image.
   - Stores image metadata (filename, description) in MongoDB.

4. **Web Search**:
   - Allows users to perform a web search, retrieves top links, and generates an AI summary of the search results.

5. **Sentiment Analysis** (Bonus Feature):
   - Analyzes user input and detects sentiment (positive/negative/neutral) using a sentiment analysis model.
   - Displays corresponding emojis based on the sentiment.

## Requirements

- Python 3.12+
- MongoDB (for storing user data, chat history, and file metadata)
- API keys for:
  - Telegram Bot API
  - Gemini API (or alternative API used for text generation and image analysis)
  - Hugging Face API (for sentiment analysis)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-ai-chatbot.git
