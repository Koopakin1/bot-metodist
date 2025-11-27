import os
from typing import Optional


# Основные настройки
BOT_TOKEN: str = os.getenv('BOT_TOKEN', 'your_bot_token_here')
APP_NAME: str = os.getenv('APP_NAME', 'Telegram Bot')
DEBUG: bool = os.getenv('DEBUG', 'False').lower() == 'true'

# Настройки базы данных
DATABASE_PATH: str = os.getenv('DATABASE_PATH', 'data/database.db')
DATABASE_URL: str = os.getenv('DATABASE_URL', f'sqlite:///{DATABASE_PATH}')

# Настройки логирования
LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE: str = os.getenv('LOG_FILE', 'logs/app.log')

# Настройки Redis (если используется)
REDIS_HOST: str = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT: int = int(os.getenv('REDIS_PORT', '6379'))
REDIS_DB: int = int(os.getenv('REDIS_DB', '0'))
REDIS_PASSWORD: Optional[str] = os.getenv('REDIS_PASSWORD', None)

# Настройки кэширования
CACHE_TTL: int = int(os.getenv('CACHE_TTL', '3600'))  # Время жизни кэша в секундах

# Настройки API
API_BASE_URL: str = os.getenv('API_BASE_URL', 'https://api.telegram.org/bot')
REQUEST_TIMEOUT: int = int(os.getenv('REQUEST_TIMEOUT', '30'))

# Настройки файлов
UPLOAD_FOLDER: str = os.getenv('UPLOAD_FOLDER', 'uploads/')
MAX_CONTENT_LENGTH: int = int(os.getenv('MAX_CONTENT_LENGTH', '16777216'))  # 16MB
ALLOWED_EXTENSIONS: set = set(os.getenv('ALLOWED_EXTENSIONS', 'txt,pdf,doc,docx,jpg,jpeg,png').split(','))

# Настройки безопасности
SECRET_KEY: str = os.getenv('SECRET_KEY', 'your-secret-key-here')
JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')
JWT_ACCESS_TOKEN_EXPIRES: int = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '15'))  # В минутах
JWT_REFRESH_TOKEN_EXPIRES: int = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', '30'))  # В днях

# Настройки почты (если используется)
MAIL_SERVER: str = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT: int = int(os.getenv('MAIL_PORT', '587'))
MAIL_USE_TLS: bool = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
MAIL_USERNAME: Optional[str] = os.getenv('MAIL_USERNAME', None)
MAIL_PASSWORD: Optional[str] = os.getenv('MAIL_PASSWORD', None)
MAIL_DEFAULT_SENDER: Optional[str] = os.getenv('MAIL_DEFAULT_SENDER', None)

# Настройки внешних сервисов
EXTERNAL_API_KEY: Optional[str] = os.getenv('EXTERNAL_API_KEY', None)
EXTERNAL_API_URL: str = os.getenv('EXTERNAL_API_URL', 'https://external-api.example.com')

# Настройки хранения данных
DATA_RETENTION_DAYS: int = int(os.getenv('DATA_RETENTION_DAYS', '365'))  # Количество дней хранения данных

# Настройки производительности
WORKER_COUNT: int = int(os.getenv('WORKER_COUNT', '4'))
MAX_CONNECTIONS: int = int(os.getenv('MAX_CONNECTIONS', '100'))

# Настройки уведомлений
NOTIFICATION_TEMPLATES_DIR: str = os.getenv('NOTIFICATION_TEMPLATES_DIR', 'templates/notifications/')

# Путь к директории с медиафайлами
MEDIA_PATH: str = os.getenv('MEDIA_PATH', 'media/')

# Настройки реферальной системы
REFERRAL_CODE_LENGTH: int = int(os.getenv('REFERRAL_CODE_LENGTH', '6'))
REFERRAL_REWARD_AMOUNT: int = int(os.getenv('REFERRAL_REWARD_AMOUNT', '100'))