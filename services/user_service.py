class UserService:
    """
    Сервис для работы с пользователями
    """
    
    def __init__(self):
        """
        Инициализация сервиса пользователей
        ""
        pass
    
    async def create_user(self, user_data: dict):
        """
        Создание нового пользователя
        :param user_data: Данные пользователя
        :return: Информация о созданном пользователе
        ""
        pass
    
    async def get_user_by_id(self, user_id: int):
        """
        Получение пользователя по ID
        :param user_id: ID пользователя
        :return: Информация о пользователе
        ""
        pass
    
    async def get_user_by_telegram_id(self, telegram_id: int):
        """
        Получение пользователя по Telegram ID
        :param telegram_id: Telegram ID пользователя
        :return: Информация о пользователе
        ""
        pass
    
    async def update_user(self, user_id: int, update_data: dict):
        """
        Обновление информации о пользователе
        :param user_id: ID пользователя
        :param update_data: Данные для обновления
        :return: Обновленная информация о пользователе
        ""
        pass
    
    async def delete_user(self, user_id: int):
        """
        Удаление пользователя
        :param user_id: ID пользователя
        :return: Результат удаления
        ""
        pass
    
    async def get_all_users(self):
        """
        Получение списка всех пользователей
        :return: Список пользователей
        ""
        pass