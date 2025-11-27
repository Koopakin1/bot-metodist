import asyncio
import logging
import time
from contextlib import asynccontextmanager
from typing import Dict

from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession

from config.settings import BOT_TOKEN, DEBUG, LOG_LEVEL, LOG_FILE
from utils.database import init_database
from services.user_service import UserService
from services.referral_service import ReferralService
from services.file_service import FileService


# Настройка логирования
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class BotApplication:
    """
    Класс приложения Telegram-бота
    """
    
    def __init__(self):
        self.bot = None
        self.dispatcher = None
        self.user_service = UserService()
        self.referral_service = ReferralService()
        self.file_service = FileService()
        
        # Хранилище состояний пользователей (в реальном приложении лучше использовать Redis или базу данных)
        self.user_states: Dict[int, dict] = {}
    
    async def initialize(self):
        """
        Инициализация приложения
        """
        logger.info("Инициализация приложения...")
        
        # Инициализация базы данных
        init_database()
        logger.info("База данных инициализирована")
        
        # Инициализация бота
        session = AiohttpSession()
        self.bot = Bot(token=BOT_TOKEN, session=session)
        self.dispatcher = Dispatcher()
        
        # Регистрация обработчиков
        self._register_handlers()
        
        logger.info("Приложение инициализировано")
    
    def _register_handlers(self):
        """
        Регистрация обработчиков команд и сообщений
        """
        # Обработчик команды /start
        @self.dispatcher.message(lambda message: message.text == '/start')
        async def start_command_handler(message: types.Message):
            await self._handle_start_command(message)
        
        # Обработчик аудиосообщений
        @self.dispatcher.message(lambda message: message.voice is not None)
        async def audio_message_handler(message: types.Message):
            await self._handle_audio_message(message)
        
        # Обработчик документов и фото
        @self.dispatcher.message(lambda message: message.document is not None or message.photo is not None)
        async def materials_handler(message: types.Message):
            await self._handle_materials(message)
        
        # Обработчик сообщений, связанных с программами
        @self.dispatcher.message(lambda message: 'программа' in message.text.lower() if message.text else False)
        async def program_handler(message: types.Message):
            await self._handle_program_request(message)
        
        # Обработчик сообщений, связанных с рефералами
        @self.dispatcher.message(lambda message: 'реферал' in message.text.lower() if message.text else False)
        async def referral_handler(message: types.Message):
            await self._handle_referral_request(message)
        
        # Обработчик всех остальных сообщений
        @self.dispatcher.message()
        async def general_message_handler(message: types.Message):
            await self._handle_general_message(message)
    
    async def _handle_start_command(self, message: types.Message):
        """
        Обработка команды /start
        """
        user_id = message.from_user.id
        logger.info(f"Получена команда /start от пользователя {user_id}")
        
        # Проверка или создание пользователя
        user = await self.user_service.get_user_by_telegram_id(user_id)
        if not user:
            # Создание нового пользователя
            user_data = {
                'telegram_id': user_id,
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name
            }
            user = await self.user_service.create_user(user_data)
            logger.info(f"Создан новый пользователь с ID {user_id}")
        
        # Отправка приветственного сообщения
        await message.answer("Привет! Добро пожаловать в бота.")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'greeted', time.time())
        
        # Автоматическая отправка аудиофайла через 4 секунды
        await asyncio.sleep(4)
        await self._send_introduction_audio(message)
    
    async def _send_introduction_audio(self, message: types.Message):
        """
        Отправка вводного аудиофайла пользователю
        """
        user_id = message.from_user.id
        logger.info(f"Отправка вводного аудиофайла пользователю {user_id}")
        
        # В реальном приложении здесь будет отправка реального аудиофайла
        await message.answer("🎵 Вот вводное аудио для ознакомления.")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'received_audio', time.time())
        
        # Автоматическое предложение загрузить материалы через 2 секунды
        await asyncio.sleep(2)
        await self._suggest_materials_upload(message)
    
    async def _suggest_materials_upload(self, message: types.Message):
        """
        Предложение пользователю загрузить материалы
        """
        user_id = message.from_user.id
        logger.info(f"Предложение пользователю {user_id} загрузить материалы")
        
        await message.answer("Вы можете загрузить дополнительные материалы (документы, фото), которые помогут создать персональную программу.")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'awaiting_materials', time.time())
    
    async def _handle_audio_message(self, message: types.Message):
        """
        Обработка аудиосообщений
        """
        user_id = message.from_user.id
        logger.info(f"Получено аудиосообщение от пользователя {user_id}")
        
        await message.answer("Получено аудиосообщение.")
    
    async def _handle_materials(self, message: types.Message):
        """
        Обработка загруженных материалов
        """
        user_id = message.from_user.id
        logger.info(f"Получены материалы от пользователя {user_id}")
        
        await message.answer("Материалы получены. Спасибо!")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'materials_received', time.time())
        
        # Уведомление о создании индивидуальной программы
        await self._notify_program_creation(message)
    
    async def _notify_program_creation(self, message: types.Message):
        """
        Уведомление о создании индивидуальной программы
        """
        user_id = message.from_user.id
        logger.info(f"Уведомление пользователя {user_id} о создании индивидуальной программы")
        
        await message.answer("Ваша индивидуальная программа будет создана в ближайшее время.")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'program_notified', time.time())
        
        # Выдача уникальной реферальной ссылки
        await self._provide_referral_link(message)
    
    async def _provide_referral_link(self, message: types.Message):
        """
        Выдача уникальной реферальной ссылки пользователю
        """
        user_id = message.from_user.id
        logger.info(f"Выдача реферальной ссылки пользователю {user_id}")
        
        # Генерация реферального кода
        referral_code = await self.referral_service.create_referral_code(user_id)
        referral_link = f"https://t.me/your_bot_username?start={referral_code}"
        
        await message.answer(f"Ваша уникальная реферальная ссылка: {referral_link}")
        
        # Установка состояния пользователя
        self._set_user_state(user_id, 'referral_provided', time.time())
    
    async def _handle_program_request(self, message: types.Message):
        """
        Обработка запросов, связанных с программами
        """
        user_id = message.from_user.id
        logger.info(f"Получен запрос к программе от пользователя {user_id}")
        
        await message.answer("Запрос к программе обработан.")
    
    async def _handle_referral_request(self, message: types.Message):
        """
        Обработка запросов, связанных с рефералами
        """
        user_id = message.from_user.id
        logger.info(f"Получен запрос к рефералу от пользователя {user_id}")
        
        await message.answer("Запрос к рефералу обработан.")
    
    async def _handle_general_message(self, message: types.Message):
        """
        Обработка всех остальных сообщений
        """
        user_id = message.from_user.id
        logger.info(f"Получено общее сообщение от пользователя {user_id}")
        
        # В зависимости от состояния пользователя можно отправлять соответствующие ответы
        state = self._get_user_state(user_id)
        if state and state.get('state') == 'awaiting_materials':
            await message.answer("Спасибо за сообщение. Загрузите материалы (документы или фото), чтобы мы могли создать для вас индивидуальную программу.")
        else:
            await message.answer("Спасибо за сообщение. Используйте /start для начала работы с ботом.")
    
    def _set_user_state(self, user_id: int, state: str, timestamp: float = None):
        """
        Установка состояния пользователя
        """
        if user_id not in self.user_states:
            self.user_states[user_id] = {}
        
        self.user_states[user_id]['state'] = state
        self.user_states[user_id]['timestamp'] = timestamp or time.time()
    
    def _get_user_state(self, user_id: int):
        """
        Получение состояния пользователя
        """
        return self.user_states.get(user_id, None)


@asynccontextmanager
async def lifespan(app: BotApplication):
    """
    Управление жизненным циклом приложения
    ""
    logger.info("Инициализация приложения...")
    await app.initialize()
    logger.info("Приложение инициализировано")
    
    yield
    
    logger.info("Завершение работы приложения")


async def main():
    ""
    Основная функция запуска бота
    """
    logger.info("Запуск бота...")
    
    # Проверка наличия токена
    if not BOT_TOKEN or BOT_TOKEN == 'your_bot_token_here':
        logger.error("Не задан BOT_TOKEN в настройках")
        return
    
    # Создание экземпляра приложения
    app = BotApplication()
    
    # Инициализация приложения
    await app.initialize()
    
    # Запуск бота
    try:
        logger.info("Начало polling...")
        await app.bot.delete_webhook(drop_pending_updates=True)
        await app.dispatcher.start_polling(app.bot, allowed_updates=app.dispatcher.resolve_used_update_types())
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        if app.bot:
            await app.bot.session.close()
        logger.info("Сессия бота закрыта")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")