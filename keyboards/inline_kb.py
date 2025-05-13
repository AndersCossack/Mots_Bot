from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Відправити шахед на московію", callback_data="shahed"), InlineKeyboardButton(text="Запустити ракету на московію", callback_data='rocket')],
    [InlineKeyboardButton(text="Бойові Гусаки, готуйсь до вильоту!", callback_data="gus")]
])