import asyncio
import logging
from aiogram import executor, types

from bot import bot, dp, handlers
from bot.handlers.messages import platforms


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
