class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAY = 3600
    ALGORITHM = 'HS256'
    SECRET_KEY = '249y823r9v8238r9u'
