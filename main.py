from telegram import Update
from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv

# load api key  
load_dotenv()

API_KEY = os.getenv(token='API_KEY')

def start(update, context):
    update.message.reply_text("Welcome, how can I help you Today?")

def main():
    updater = Updater(token=API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
   # dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()