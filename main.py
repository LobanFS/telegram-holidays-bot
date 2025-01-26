import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler
from holidays_parser import get_today_holidays
from commands import *

load_dotenv()
def main():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token)
    dispatcher = updater.dispatcher

    #Обработка команд
    dispatcher.add_handler(CommandHandler("holidays", holidays))

    #Запуск
    updater.start_polling()
    updater.idle()





