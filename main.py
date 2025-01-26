import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Application
from commands import *

load_dotenv()
def main():
    token = os.getenv("TELEGRAM_TOKEN")
    application = Application.builder().token(token).build()
    #Обработка команд
    application.add_handler(CommandHandler("holidays", holidays))
    application.add_handler(CommandHandler("start", start))
    #Запуск
    application.run_polling()
if __name__ == '__main__':
    main()






