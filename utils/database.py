import sqlite3
from typing import Optional
from config.settings import DATABASE_PATH


class DatabaseConnection:
    """Класс для управления подключением к базе данных""
    
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self):
        """Открывает подключение к базе данных"""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Для доступа колонкам по имени
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрывает подключение к базе данных"""
        if self.connection:
            self.connection.close()


def init_database():
    """Инициализация базы данных - создание таблиц"""
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        
        # Пример создания таблицы пользователей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Пример создания таблицы рефералов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER,
                referred_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (referrer_id) REFERENCES users (id),
                FOREIGN KEY (referred_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()


def get_db_connection():
    ""Функция для получения подключения к базе данных"""
    return DatabaseConnection()