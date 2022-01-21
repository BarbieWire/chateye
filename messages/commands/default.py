from loader import dp
from aiogram.types import Message
from buttons.keyboard import PERSON


async def start(message: Message):
    await message.answer(text=F"Hi {message.chat.full_name}")
    await message.answer(text="To start click button\n *🗣find interlocutor*\n Or /help - for more information",
                         parse_mode="markdown", reply_markup=PERSON)


async def help_command(message: Message):
    await message.answer(text="Just try to find someone here and don't forget to be polite\n"
                              "Have a nice day, my friend🌛 \n\nHere's my telegram for some case:\n"
                              "t.me/barbiewire", reply_markup=PERSON, parse_mode="Markdown")


def register_default_commands():
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
