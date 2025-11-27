import logging
from aiogram import Router, types

router = Router()
logger = logging.getLogger(__name__)

@router.message(lambda message: 'реферал' in message.text.lower() if message.text else False)
async def referral_handler(message: types.Message):
    """
    Обработка запросов, связанных с рефералами
    ""
    await message.answer("Запрос к рефералу обработан.")