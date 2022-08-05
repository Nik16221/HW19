from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):  # Получаем жанр по ID
        return self.dao.get_one(bid)

    def get_all(self):  # Получаем все жанры
        return self.dao.get_all()

    def create(self, genre_d):  # Добавляем жанр
        return self.dao.create(genre_d)

    def update(self, genre_d):  # Редактируем жанр
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):  # Удаляем жанр
        self.dao.delete(rid)
