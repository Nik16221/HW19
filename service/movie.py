from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):  # Получаем фильм(используя фильтры)
        return self.dao.get_one(bid)

    def get_all(self, filters):  #
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):  # Добавляем фильм
        return self.dao.create(movie_d)

    def update(self, movie_d):  # Редактируем информацию о фильме
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):  # Удаляем фильм
        self.dao.delete(rid)
