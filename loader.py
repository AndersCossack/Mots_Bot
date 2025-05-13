from aiogram import Bot, Dispatcher
import configparser


config = configparser.ConfigParser()
config.read('data/config.ini')

API_BOT = config.get('bot', 'API_BOT').strip()

bot = Bot(API_BOT, parse_mode="HTML")
dp = Dispatcher()
