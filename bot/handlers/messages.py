from aiogram.types import Message
from bot import dp, bot
from bot.api.likee import LikeeAPI
from bot.api.tiktok import TikTokAPI
from bot.exception import HandleException


tiktok = TikTokAPI()
likee = LikeeAPI()
platforms = [tiktok, likee]


@dp.message_handler(commands='start')
async def cmd_start(message: Message):
    """Приветственное сообщение"""
    await message.answer(f"Hello {message.from_user.id}")


@dp.message_handler(content_types=['text'])
async def get_message(message: Message):
    for api in platforms:
        for video in await api.handle_message(message):
            if video:
                if video.content:
                    await bot.send_video(
                        message.chat.id, video.content,
                        reply_to_message_id=message.message_id
                    )
                elif video.url:
                    await bot.send_message(
                        message.chat.id, video.url,
                        reply_to_message_id=message.message_id
                    )
            else:

                await bot.send_message(
                    message.chat.id, reply_to_message_id=message.message_id
                )
