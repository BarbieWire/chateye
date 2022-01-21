from loader import dp, bot
from aiogram.types import Message
from database.control import Database
import os
from aiogram.dispatcher import filters
from buttons.keyboard import CANCEL, STOP, PERSON
from dotenv import load_dotenv

load_dotenv(".env")
HOST, DATABASE, USER, PASSWORD = os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USER"), os.getenv("PASSWORD")


async def start_conversation(message: Message):
    if message.text == "🗣Find interlocutor":
        await message.answer(text="Searching, but you can cancel anyway...", reply_markup=CANCEL)

        try:
            connection = Database(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
            queue = Database.get_queue(connection, table="queue")
            if len(queue) == 1:
                Database.insert(connection, "dialogs", message.from_user.id, queue[0][1])
                Database.delete_queue(connection, chat_id=queue[0][1])
                await bot.send_message(chat_id=message.from_user.id, text="✔️the interlocutor was found",
                                       reply_markup=STOP)
                await bot.send_message(chat_id=queue[0][1], text="✔️the interlocutor was found", reply_markup=STOP)
                return True
            else:
                raise ValueError("ValueError")

        except Exception as _ex:
            connection = Database(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
            Database.create(connection, message.from_user.id, table="queue")

    if message.text == "❌Cancel":
        connection = Database(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
        if Database.queue_check(connection=connection, chat_id=message.from_user.id, table="queue") is True:
            Database.delete_queue(connection, chat_id=message.from_user.id)
            await message.answer(text="❌Cancel", reply_markup=PERSON)
        else:
            await message.answer(text="No dialogs found...")

    if message.text == "⛔Stop dialog":
        connection = Database(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
        data = Database.dialogs_check(connection, message.from_user.id)
        if data[0] is True:
            if data[1] == 2:
                Database.firstuser(connection, chat_id=message.from_user.id)
                await message.answer(text='❌you just quit', reply_markup=PERSON)
                await bot.send_message(chat_id=data[2], text='interlocutor left chat', reply_markup=PERSON)
            if data[1] == 1:
                Database.seconduser(connection, chat_id=message.from_user.id)
                await message.answer(text='❌you just quit', reply_markup=PERSON)
                await bot.send_message(chat_id=data[2], text='interlocutor left chat', reply_markup=PERSON)
        else:
            await message.answer(text="❌No dialogs found...")


async def dialog(message: Message):
    connection = Database(host=HOST, database=DATABASE, user=USER, password=PASSWORD).connect()
    data = Database.dialogs_check(connection=connection, chat_id=message.from_user.id)
    if message.content_type == "text":
        try:
            await bot.send_message(chat_id=int(data[2]), text=message["text"])
        except Exception as _ex:
            await message.answer(text="❌Unknown command")

    elif message.content_type == "photo":
        try:
            photo = message.photo[0].file_id
            await bot.send_photo(chat_id=int(data[2]), photo=photo)
        except Exception as _ex:
            await message.answer(text="❌Unknown command")
            print(_ex)
    else:
        await message.answer(text="impossible to send content")


def register_message_handlers():
    dp.register_message_handler(
        start_conversation, filters.Text(equals=["🗣Find interlocutor", "❌Cancel", "⛔Stop dialog"], ignore_case=True)
    )
    dp.register_message_handler(dialog, content_types=["any"])
