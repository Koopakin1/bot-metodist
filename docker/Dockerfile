# Используем официальный образ Python
FROM python:3.11-slim
# Установка переменных окружения
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Установка рабочей директории
WORKDIR /app

# Копирование файла зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Создание директорий для данных и логов
RUN mkdir -p data logs uploads media

# Установка прав доступа
RUN chmod +x /app/src/bot/main.py
# Точка входа
CMD ["python", "-m", "src.bot.main"]