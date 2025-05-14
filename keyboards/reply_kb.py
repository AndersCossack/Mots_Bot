from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



reply_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    [KeyboardButton(text="Підтримка"), KeyboardButton(text="Про мене")],
    [KeyboardButton(text="Назад"), KeyboardButton(text='Прибрати клавіатуру')],
], resize_keyboard=True, one_time_keyboard=True)
   
