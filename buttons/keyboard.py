from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


PERSON = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="🗣Find interlocutor")
)

CANCEL = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="❌Cancel")
)

STOP = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="⛔Stop dialog")
)
