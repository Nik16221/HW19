import jwt
from flask import request, current_app

from implemented import user_service


# Декоратор для авторизации(проверки токена)
def auth_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.environ.get("AUTHORIZATION").replace("Bearer ", "")

        if not token:
            return "Токен не найден"

        try:
            jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithms=current_app.config["ALGORITHM"])
            return func(*args, **kwargs)

        except Exception:
            raise Exception

    return wrapper


# Декоратор для проверки роли Userа
def admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers["AUTHORIZATION"].split("Bearer ")[-1]

        if not token:
            return "Токен не найден"

        try:
            data = jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithms=current_app.config["ALGORITHM"])

            if user_service.get_by_username(data["username"]).role == "admin":
                return func(*args, **kwargs)

            else:
                return "У вас нет доступа"

        except Exception as e:
            print("JWT Decode Exception", e)

    return wrapper
