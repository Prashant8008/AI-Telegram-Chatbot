import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["bot-user-data"]

# Collections
users = db["users"]
chats = db["chats"]
files = db["files"]

def save_user(user_data):
    try:
        users.update_one(
            {"chat_id": user_data["chat_id"]},
            {"$set": user_data},
            upsert=True
        )
    except Exception as e:
        print(f"DB Error: {e}")

def save_chat(chat_data):
    chats.insert_one(chat_data)

def save_file(file_data):
    files.insert_one(file_data)

if __name__ == "__main__":
    try:
        client.server_info()  # Test connection
        print("✅ Connected to MongoDB!")
        
        # Test saving user data
        user_data = {
            "chat_id": 123456789,
            "username": "prashant",
            "first_name": "Prashant",
            "last_name": "Choudhary",
            "language_code": "en"
        }
        save_user(user_data)
        print("✅ User data saved!")
        
        # Test saving chat data
        chat_data = {
            "chat_id": 123456789,
            "message": "Hello, this is a test message!",
            "timestamp": "2025-01-29T15:00:00Z"
        }
        save_chat(chat_data)
        print("✅ Chat data saved!")
        
        # Test saving file data
        file_data = {
            "file_id": "abc123xyz",
            "file_name": "test_file.jpg",
            "file_size": 2048,
            "upload_date": "2025-01-29"
        }
        save_file(file_data)
        print("✅ File data saved!")
    
    except Exception as e:
        print(f"❌ Connection failed: {e}")