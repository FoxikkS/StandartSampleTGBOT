from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram import F, Router

callback_router = Router()

@callback_router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery):
    await callback.answer()