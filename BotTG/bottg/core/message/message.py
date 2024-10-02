from aiogram.filters import CommandStart, Command
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter
from utils.loaderJSON import configJSON
from database.models import User

message_router = Router()

@message_router.message(CommandStart)
async def start(message: Message):
    ...
