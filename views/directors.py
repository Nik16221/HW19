from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    def get(self):
        """
        Выгружаем из базы всех режессеров
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def post(self):
        data = request.json
        return DirectorSchema().dump(director_service.create(data)), 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    def get(self, rid):
        """
        Выгружаем из базы режессера по id
        """
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def put(self, pk):
        data = request.json
        if not data.get["id"] or data.get["id"] != pk:
            data.get["id"] = pk
        return director_service.update(data), 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def delete(self, pk):
        return director_service.delete(pk)
