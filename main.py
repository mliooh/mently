from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# load api key  
load_dotenv()

api_key = os.getenv('API_KEY')
application = ApplicationBuilder().token(api_key).build()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome, how can I help you Today?")


application.add_handler(CommandHandler('start', start))
    
    
   
    

if __name__ == '__main__':
    application.run_polling()
