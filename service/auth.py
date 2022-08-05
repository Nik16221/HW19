import base64
import calendar
import datetime
import hashlib

import jwt
from flask import current_app


# Создаем хеш для пароля
def generate_password(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",  # Хеш алгоритм
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],  # приставка к Хешу
        iterations=current_app.config["PWD_HASH_ITERATIONS"]  # Количество итераций
    )


# Представляем хеш в виде строки, декодируем с помощью UTF-8
def generate_password_hash(password):
    return base64.b64encode(generate_password(password)).decode("utf-8")


# Сравниваем Хеш пароль с паролем при авторизации
def compare_password_hash(password_hash, other_password):
    return password_hash == generate_password_hash(other_password)


# Генерируем токен
def generate_token(username, password_hash, password, is_refresh=False):
    if username is None:
        return "Такого пользователя нет"
    if not is_refresh:
        if not compare_password_hash(password_hash=password_hash, other_password=password):
            return "Что-то пошло не так"
    # В токене храним информацию: логин и пароль
    data = {
        "username": username,
        "password": password
    }
    # Временный токен
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config["TOKEN_EXPIRE_MINUTES"])
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, key=current_app.config["SECRET_KEY"], algorithm=current_app.config["ALGORITHM"])

    # Обновляем токен для длительного доступа
    min_day = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config["TOKEN_EXPIRE_DAY"])
    data["exp"] = calendar.timegm(min_day.timetuple())
    refresh_token = jwt.encode(data, key=current_app.config["SECRET_KEY"], algorithm=current_app.config["ALGORITHM"])

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


# Генерируем новый токен
def approve_token(token):
    data = jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithm=current_app.config["ALGORITHM"])
    username = data.get("username")  # Получаем логин из токена
    password = data.get("password")  # Получаем пароль из токена

    return generate_token(username=username, password_hash=None, password=password, is_refresh=True)
