# Quote App
Django-приложение для управления цитатами.

## Установка
1. Клонируйте репозиторий: `git clone https://github.com/akiko9898/quote_app.git`
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте: `venv\Scripts\activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Выполните миграции: `python manage.py migrate`
6. Запустите сервер: `python manage.py runserver`

## Развертывание
См. инструкции для PythonAnywhere или ngrok.

## Использование
- `/` - случайная цитата
- `/add/` - добавление цитаты
- `/top/` - топ-10