Установка зависимостей:
    pip install -r requirements.txt
Создать файл .env в корне папки blog и записать туда переменные окружения без этого не будет работать.
- FLASK_ENV=development
- FLASK_APP=run.py
- SQLALCHEMY_DATABASE_URI=sqlite:///blog.db
- SQLALCHEMY_TRACK_MODIFICATIONS=True
- EMAIL_USER=YOUR_MAIL
- EMAIL_PASS=YOUR_PASS