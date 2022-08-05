from dao.user import UserDAO
from service.auth import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):  # Получаем пользователя по ID
        return self.dao.get_one(uid)

    def get_all(self):  # Получаем всех пользователей
        return self.dao.get_all()

    def get_by_username(self, username):  # Получаем пользователя по лоигну
        return self.dao.get_by_username(username)

    def create(self, data):  # При добавлении пользователя хешируем пароль
        data["password"] = generate_password_hash(password=data["password"])
        return self.dao.create(data)

    def update(self, data):  # Редактируем пользователя
        self.dao.update(data)
        return self.dao

    def delete(self, uid):  # Удаляем пользователя
        self.dao.delete(uid)
