import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)