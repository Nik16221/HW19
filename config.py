import base64


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'  # путь до бд
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}  # отображение русского текста
    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100000
    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAY = 1440
    ALGORITHM = "HS256"
    SECRET_KEY = '249y823r9v8238r9u'

