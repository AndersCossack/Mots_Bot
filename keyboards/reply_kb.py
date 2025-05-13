from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    [KeyboardButton(text="Підтримка"), KeyboardButton(text="Про мене")],
    [KeyboardButton(text="Назад")],
], resize_keyboard=True)
    