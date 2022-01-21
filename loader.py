from aiogram import Dispatcher, Bot
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = getenv("BOT_TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
