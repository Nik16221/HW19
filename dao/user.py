from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):  # Получение одного
        return self.session.query(User).get(uid)

    def get_all(self):  # Получение всех
        return self.session.query(User).all()

    def get_by_username(self, username):  # Получение по логину
        return self.session.query(User).filter(User.username == username).one()

    def create(self, data):  # Создание
        ent = User(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):  # Удаление
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, data):  # Редактирование, если поле пустое - его редактировать не надо.
        user = self.get_one(data.get("id"))
        if data.get("username"):
            user.username = data.get("username")
        if data.get("password"):
            user.password = data.get("password")
        if data.get("role"):
            user.role = data.get("role")

        self.session.add(user)
        self.session.commit()
