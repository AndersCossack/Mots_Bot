from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject

from database.database import get_db_connection
from datetime import datetime

from handlers.wordsdic import HELLO_RESPONSES, help_text, about_text
import keyboards.reply_kb as rkb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id 
    username = message.from_user.username or 'None'
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or 'None'
    time_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = await get_db_connection()

    try:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
            if await cursor.fetchone() is None:
                await cursor.execute('INSERT INTO users (user_id, username, first_name, last_name, time_added) VALUES (?, ?, ?, ?, ?)', (user_id, username, first_name, last_name, time_added))
                await conn.commit() 
                await message.answer('Привіт! Я готовий допомагати!')
    finally:
        await conn.close()

        
"""
@router.message(Command('myinfo'))
async def cmd_myinfo(message: Message, db):
    user_id = message.from_user.id

    async with db.cursor() as cursor:
        await cursor.execute('SELECT user_id, username, first_name, last_name, time_added FROM users WHERE user_id = ?', (user_id,))
        user_info = await cursor.fetchone()

    if user_info is None:
        await message.answer('Користувач не знайдений')
        return
    
    message_text = (
            f'ID: {user_info[0]}\n'
            f'Username: {user_info[1]}\n'
            f'First Name: {user_info[2]}\n'
            f'Last Name: {user_info[3]}\n'
            f'Time Added: {user_info[4]}\n'
        )

    await message.answer(message_text)
"""

@router.message(Command('myinfo'))
async def cmd_myinfo(message: Message):
    user_id = message.from_user.id
    conn = await get_db_connection()
    try:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT user_id, username, first_name, last_name, time_added FROM users WHERE user_id = ?', (user_id,))
            user_info = await cursor.fetchone()

            if user_info is None:
                await message.answer('Користувач не знайдений')
                return
            
            message_text = (
                f'ID: {user_info[0]}\n'
                f'Username: {user_info[1]}\n'
                f'First Name: {user_info[2]}\n'
                f'Last Name: {user_info[3]}\n'
                f'Time Added: {user_info[4]}\n'
            )

            await message.answer(message_text)
    finally:
        await conn.close()



@router.message(Command('update_username'))
async def cmd_update(message: Message, command: CommandObject):
    user_id = message.from_user.id
    new_username = command.args

    conn = None

    try:
        if not new_username:
            await message.answer('Вкажіть нове імʼя')
            return
        
        conn = await get_db_connection()
        async with conn.cursor() as cursor:
            await cursor.execute('UPDATE users SET username = ? WHERE user_id = ?', (new_username, user_id))
            await conn.commit()

        await message.answer(f'Ваше імʼя оновлене на: {new_username}')
    finally:
        if conn:
            await conn.close()

    

@router.message(Command('delete_me'))
async def delete_me(message: Message):
    user_id = message.from_user.id

    conn = await get_db_connection()
    async with conn.cursor() as cursor:
        await cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        await conn.commit()
    await cursor.close()
    await conn.close() 

    await message.answer('Ваш запис видалений')



"""
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привіт! Я готовий допомагати!")
"""

@router.message(Command('help'))
async def cmd_help(message: Message):    
    await message.answer(help_text)


@router.message(Command('keyboard'))
async def cmd_keyboard(message: Message):
    await message.answer('Слухаю', reply_markup=rkb.reply_menu)


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
    elif message.new_chat_members:
        await message.answer('Здоровеньки були')
    else:
        await message.answer("Отримано повідомлення невизначеного типу")
