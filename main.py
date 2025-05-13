import asyncio
from loader import bot, dp

from handlers.commands import router as commands_router
from handlers.callback import call_router

async def main():
    try:
        print("Bot Start")

        await  bot.delete_webhook(drop_pending_updates=True)
        print('Webhook deleted')

        dp.include_router(call_router)
        dp.include_router(commands_router)
        
        await dp.start_polling(bot)
    except Exception as ex:
        print(f"There is an Exception {ex}")
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")






