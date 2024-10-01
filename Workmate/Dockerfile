# Dockerfile
FROM python:3.9

WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]