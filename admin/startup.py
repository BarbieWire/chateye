from aiogram.types import Message
from loader import bot
import os
from dotenv import load_dotenv

load_dotenv(".env")
ADMINS = [os.getenv("ADMINS")]


async def startup(message: Message):
    for chat in ADMINS:
        await bot.send_message(chat_id=chat, text="bot just started")


async def shutdown(message: Message):
    for chat in ADMINS:
        await bot.send_message(chat_id=chat, text="goodbye")
