from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from database import save_user, save_chat, save_file
from gemini import generate_text, analyze_image

load_dotenv()

# Initialize bot
application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

# ---- Handlers ----
async def start(update: Update, context):
    contact_btn = KeyboardButton("Share Contact 📱", request_contact=True)
    keyboard = ReplyKeyboardMarkup([[contact_btn]], resize_keyboard=True, one_time_keyboard=True)
    await update.message.reply_text("👋 Welcome! Please share your contact:", reply_markup=keyboard)

async def handle_contact(update: Update, context):
    user = update.effective_user
    contact = update.message.contact
    
    # Save user data
    user_data = {
        "chat_id": user.id,
        "first_name": user.first_name,
        "username": user.username,
        "phone": contact.phone_number
    }
    save_user(user_data)
    
    await update.message.reply_text("✅ Registration complete! Ask me anything.")

async def handle_text(update: Update, context):
    user_input = update.message.text
    chat_id = update.effective_chat.id
    
    try:
        # Generate response using Gemini
        response = await generate_text(user_input)

        # Save chat history
        save_chat({
            "chat_id": chat_id,
            "user_input": user_input,
            "bot_response": response,
            "timestamp": update.message.date
        })

        # Send response to user
        await update.message.reply_text(response)

    except Exception as e:
        await update.message.reply_text("❌ Error processing request. Try again later.")

async def handle_image(update: Update, context):
    file = await update.message.photo[-1].get_file()
    image_url = file.file_path
    
    # Analyze image with Gemini
    analysis = await analyze_image(image_url)
    
    # Save file metadata
    save_file({
        "chat_id": update.effective_chat.id,
        "filename": file.file_id,
        "description": analysis,
        "timestamp": update.message.date
    })
    
    await update.message.reply_text(f"📸 Analysis:\n\n{analysis}")

# Register Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
application.add_handler(MessageHandler(filters.PHOTO, handle_image))

if __name__ == "__main__":
    application.run_polling()
