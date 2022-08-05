from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid): #Получение одного
        return self.session.query(Director).get(bid)

    def get_all(self): #Получение всех
        return self.session.query(Director).all()

    def create(self, director_d): #Создание
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid): #Удаление
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d): #Редактирование
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
