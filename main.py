from loader import dp
from aiogram import executor
from admin.startup import shutdown, startup
from messages.commands import default
from messages.message import dialog


default.register_default_commands()
dialog.register_message_handlers()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=startup, on_shutdown=shutdown)
