import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, Application
from holidays_parser import get_today_holidays
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






