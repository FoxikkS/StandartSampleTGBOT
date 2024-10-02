from utils.loaderINI import Config
from splogger import SPinfo
from core.message.handlers.callback import callback_router
from core.message.message import message_router
from aiogram import Dispatcher, Bot   
from aiogram.fsm.storage.memory import MemoryStorage
from tortoise import Tortoise

bot = Bot(Config().token)
dp = Dispatcher()
storage = MemoryStorage()

async def start_polling():
    dp.include_router(message_router) and dp.include_router(callback_router)
    SPinfo('Подготовка запуска базы данных...')
    await Tortoise.init(
        db_url='',
        modules={'models': ['database.models']}
    )
    SPinfo('Успешно!')
    await Tortoise.generate_schemas()
    await dp.start_polling(bot, skip_update=True)