import logging
from aiogram import Router, types

router = Router()
logger = logging.getLogger(__name__)

@router.message(lambda message: 'программа' in message.text.lower() if message.text else False)
async def program_handler(message: types.Message):
    """
    Обработка запросов, связанных с программами
    ""
    await message.answer("Запрос к программе обработан.")