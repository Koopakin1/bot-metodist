import logging
from aiogram import Router, types

router = Router()
logger = logging.getLogger(__name__)

@router.message(lambda message: message.document or message.photo)
async def materials_handler(message: types.Message):
    """
    Обработка материалов (документов, фото)
    ""
    await message.answer("Получен материал.")