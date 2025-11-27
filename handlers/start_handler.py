import logging
from aiogram import Router, types
from aiogram.filters import Command

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command("start"))
async def start_handler(message: types.Message):
    """
    Обработка команды /start
    ""
    await message.answer("Привет! Добро пожаловать в бота.")