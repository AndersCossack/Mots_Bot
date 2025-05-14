from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv



load_dotenv(override=True)

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError('Token not found! Check your .env file and make sure TOKEN is set.')

bot = Bot(TOKEN)
dp = Dispatcher()
