import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers.registration import router as registration_router
from handlers.food_analysis import router as food_analysis_router

from utils.logger import setup_logging

import logging



async def main():
    
    setup_logging()
    logging.info("bot started")
    # logging.info("INFO: это просто информация")
    # logging.warning("WARNING: это предупреждение")
    # logging.error("ERROR: это ошибка")
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(registration_router)
    dp.include_router(food_analysis_router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
