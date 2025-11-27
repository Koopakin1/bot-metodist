import re
from typing import Any, Dict, List, Optional
from datetime import datetime


def validate_telegram_id(telegram_id: Any) -> bool:
    """
    Валидация Telegram ID
    Telegram ID - это положительное целое число
    ""
    if isinstance(telegram_id, str):
        return telegram_id.isdigit() and int(telegram_id) > 0
    elif isinstance(telegram_id, int):
        return telegram_id > 0
    return False


def validate_username(username: str) -> bool:
    """
    Валидация username Telegram
    Username должен быть длиной от 5 до 32 символов,
    содержать только латинские буквы, цифры и подчеркивание
    ""
    if not username or not isinstance(username, str):
        return False
    
    # Username должен начинаться с буквы и быть длиной 5-32 символа
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,31}$'
    return bool(re.match(pattern, username))


def validate_email(email: str) -> bool:
    """
    Валидация email адреса
    ""
    if not email or not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Валидация телефонного номера
    Принимает номера в международном формате
    ""
    if not phone or not isinstance(phone, str):
        return False
    
    # Удаляем все пробелы, тире и скобки
    cleaned_phone = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Проверяем, начинается ли номер с + и содержит ли только цифры
    pattern = r'^\+\d{10,15}$'
    return bool(re.match(pattern, cleaned_phone))


def validate_url(url: str) -> bool:
    """
    Валидация URL
    ""
    if not url or not isinstance(url, str):
        return False
    
    pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
    return bool(re.match(pattern, url))


def validate_not_empty(value: Any) -> bool:
    """
    Проверяет, что значение не пустое
    ""
    if value is None:
        return False
    if isinstance(value, str):
        return len(value.strip()) > 0
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


def validate_length(value: str, min_length: int = 0, max_length: int = None) -> bool:
    """
    Валидация длины строки
    ""
    if not isinstance(value, str):
        return False
    
    length = len(value)
    if max_length is None:
        return length >= min_length
    return min_length <= length <= max_length


def validate_choice(value: Any, choices: List[Any]) -> bool:
    """
    Проверяет, что значение находится в списке допустимых значений
    ""
    return value in choices


def validate_date(date_string: str, date_format: str = '%Y-%m-%d') -> bool:
    """
    Валидация строки даты
    ""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def validate_data(data: Dict[str, Any], rules: Dict[str, List[callable]]) -> Dict[str, List[str]]:
    """
    Валидация словаря данных по заданным правилам
    
    Args:
        data: Словарь с данными для валидации
        rules: Словарь с правилами валидации {поле: [функции_валидации]}
    
    Returns:
        Словарь с ошибками валидации {поле: [список_ошибок]}
    ""
    errors = {}
    
    for field, validators in rules.items():
        value = data.get(field)
        field_errors = []
        
        for validator in validators:
            try:
                if not validator(value):
                    field_errors.append(f"Поле '{field}' не прошло валидацию: {validator.__name__}")
            except Exception as e:
                field_errors.append(f"Ошибка валидации поля '{field}': {str(e)}")
        
        if field_errors:
            errors[field] = field_errors
    
    return errors