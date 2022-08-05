from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):  # Получаем одного режиссера по ID
        return self.dao.get_one(bid)

    def get_all(self):  # Получваем всех режессеров
        return self.dao.get_all()

    def create(self, director_d):  # Добавляем режессера
        return self.dao.create(director_d)

    def update(self, director_d):  # Редактируем режессера
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):  # Удаляем режессера
        self.dao.delete(rid)
