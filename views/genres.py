from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    # Выгружаем из базы все жанры
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    # Добавляем жанр
    def post(self):
        data = request.json
        return genre_service.create(data), 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    def get(self, rid):
        # Выгружаем из базы жанр по id
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def put(self, pk):
        # Редактируем данные о жанре
        data = request.json
        if not data.get["id"] or data.get["id"] != pk:
            data.get["id"] = pk
        return genre_service.update(data), 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def delete(self, pk):
        # Удаляем жанр
        return genre_service.delete(pk)
