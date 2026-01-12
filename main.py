import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers.registration import register_registration_handlers


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    register_registration_handlers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
