import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "545121578dsafsdfasf25sa4dfas21df54asdf12asdf54asd2fasdf4a2s0df")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","postgresql://flask_user:password@localhost:5433/flask_app")

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is not set in the environment.")
