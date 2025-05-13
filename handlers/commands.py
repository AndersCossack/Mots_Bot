from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from handlers.wordsdic import HELLO_RESPONSES, help_text, about_text
import keyboards.reply_kb as rkb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт! Я готовий допомагати!", reply_markup=rkb.reply_start)

@router.message(Command('help'))
async def cmd_help(message: Message):    
    await message.answer(help_text)


@router.message(lambda msg: msg.text and msg.text.lower() in HELLO_RESPONSES)
async def reply_hello(message: Message):
    text = message.text.lower()
    name = message.from_user.first_name
    response = HELLO_RESPONSES[text](name)
    await message.answer(response)

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(about_text)

@router.message(F.photo)
async def cmd_hello(message: Message):
    photo = message.photo
    text = "Як гарно!"
    await message.answer_photo(photo[0].file_id, text)


@router.message()
async def handler_messages(message: Message):
    if message.text:
        await message.answer("Це текстове повідомлення")
    elif message.photo:
        await message.answer("Дякую за фото!")
    elif message.video:
        await message.answer("Дякую за відео!")
    elif message.document:
        await message.answer("Дякую за документ!")
    elif message.audio:
        await message.answer("Дякую за аудіо!")
    elif message.voice:
        await message.answer("Дякую за голосове повідомлення!")
    elif message.location:
        await message.answer(f"Ви надіслали місцезнаходження: {message.location.latitude}, {message.location.longitude}")
    elif message.contact:
        await message.answer(f"Контакт: {message.contact.first_name}{message.contact.phone_number}")
    else:
        await message.answer("Отримано повідомлення невизначеного типу")
