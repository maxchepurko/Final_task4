# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install pandas

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Определяем команду для запуска скрипта
CMD ["python", "app.py"]