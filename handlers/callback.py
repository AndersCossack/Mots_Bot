from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
import asyncio

call_router = Router()

import keyboards.inline_kb as ikb


@call_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer("Чим будемо бомбити?😏", reply_markup=ikb.inline_kb)


@call_router.message(F.text == "Підтримка")
async def help(message: Message):
    await message.answer("Вам потрібна підтримка?")


@call_router.message(F.text == "Про мене")
async def about_me(message: Message):
    await message.answer("Я бот, який допомагає вам у спілкуванні. Я можу відповідати на ваші запитання та допомагати з інформацією.")


@call_router.message(F.text == "Назад")
async def back(message: Message):
    await message.answer("Ви повернулися назад до головного меню.")

@call_router.message(F.text == 'Прибрати клавіатуру')
async def remove_keyboard(message: Message):
    await message.answer('Прибрано', reply_markup=ReplyKeyboardRemove())

@call_router.callback_query(F.data == 'масква')
async def mascfa(callback: CallbackQuery):
    await callback.answer('ВЖжжЖжЖжжЖжж...')
    await asyncio.sleep(1.5)
    await callback.message.answer_animation(
        animation='https://tenor.com/view/moskva-fire-cat-gif-25387626'
    )
    await asyncio.sleep(1)
    await callback.message.answer('Прямо по кремлю!')

@call_router.callback_query(F.data == "lutiy")
async def lutiy(callback: CallbackQuery):
    await callback.answer('Заправляємо...')
    await asyncio.sleep(1.5)
    await callback.message.answer("Запустити по:", reply_markup=await ikb.city_list())
    #await callback.message.answer("Вражені позиції: \nмасква\nсаратаф\nЩе якесь село")


@call_router.callback_query(F.data == "trembita")
async def trembita(callback: CallbackQuery):
    await callback.answer('Націлюємо...')
    await asyncio.sleep(1.5)
    await callback.message.answer("Вражені позиції: \nПрилетіло по кремлю")


@call_router.callback_query(F.data == "gus")
async def gus(callback: CallbackQuery):
    await callback.answer('Підгодовуємо гусаків...')
    await asyncio.sleep(1.5)
    await callback.message.answer("Вражені позиції: \nГусаки загидили расіян")
