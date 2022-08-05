from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from service.decorators import admin_required, auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    def get(self):
        # Выгружаем все фильмы
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def post(self):
        # Добавляем фильм
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required  # Применяем декоратор для доступа после регистрации
    def get(self, bid):
        # Получаем фильм по ID
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def put(self, bid):
        # Редактируем информацию о фильме
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required  # Применяем декоратор для проверки роли(админ или нет)
    def delete(self, bid):
        # Удаляем фильм
        movie_service.delete(bid)
        return "", 204
