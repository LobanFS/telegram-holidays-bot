from selenium.webdriver.common.devtools.v85.web_audio import ContextType
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from holidays_parser import get_today_holidays

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Напиши команду /holidays")

async def holidays(update: Update, context: CallbackContext) -> None:
    holidays_list = get_today_holidays()
    if holidays_list:
        response = "Сегодня:\n" + "\n".join(holidays_list)
    else:
        response = "Проблемы с парсингом или доступом или еще чем-то :(."
    await update.message.reply_text(response)

