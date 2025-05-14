import logging
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Callable, Dict, Awaitable

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]) -> Any:
        
            if event.from_user and event.text:
                  user_id = event.from_user.id
                  command = event.text
                  logging.info(f'Користувач з id: {user_id} використав команду {command}')
            else:
                  logging.warning('Отримано повідомлення без користувача чи тексту')
            
            logging.info('До обробника')

            try:
                  res = await handler(event, data)
                  logging.info('Після обробника')
                  return res
            except Exception as e:
                  logging.error(f'Помилка при обробці повідомлення: {e}')
                  raise
    