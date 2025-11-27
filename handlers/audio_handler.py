import logging
from aiogram import Router, types

router = Router()
logger = logging.getLogger(__name__)

@router.message(lambda message: message.content_type == 'voice')
async def audio_handler(message: types.Message):
    """
    Обработка аудиосообщений
    ""
    await message.answer("Получено аудиосообщение.")