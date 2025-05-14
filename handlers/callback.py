from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

call_router = Router()

import keyboards.inline_kb as ikb


@call_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer("Виберіть пункт меню:", reply_markup=ikb.inline_kb)


@call_router.message(F.text == "Підтримка")
async def menu(message: Message):
    await message.answer("Вам потрібна підтримка?")


@call_router.message(F.text == "Про мене")
async def menu(message: Message):
    await message.answer(
        "Я бот, який допомагає вам у спілкуванні. Я можу відповідати на ваші запитання та допомагати з інформацією."
    )


@call_router.message(F.text == "Назад")
async def menu(message: Message):
    await message.answer("Ви повернулися назад до головного меню.")


@call_router.callback_query(F.data == "shahed")
async def shahed(callback: CallbackQuery):
    await callback.message.answer("Вражені позиції: \nмасква\nсаратаф\n\Ще якесь село")


@call_router.callback_query(F.data == "rocket")
async def shahed(callback: CallbackQuery):
    await callback.message.answer("Вражені позиції: \nПрилетіло по кремлю")


@call_router.callback_query(F.data == "gus")
async def shahed(callback: CallbackQuery):
    await callback.message.answer("Вражені позиції: \nГусаки загидили расіян")
