from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

list = ['масква', 'саратаф', 'краснодар']

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="БПЛА 'Лютий'", callback_data="lutiy"), InlineKeyboardButton(text="Крилата 'Трембіта'", callback_data='trembita')],
    [InlineKeyboardButton(text="Бандеро Гусі", callback_data="gus")]
])

async def city_list():
    keyboard = InlineKeyboardBuilder()
    for city in list:
        keyboard.add(InlineKeyboardButton(text=city, callback_data=city))

    return keyboard.as_markup()
