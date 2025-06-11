import os

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY", "545121578dsafsdfasf25sa4dfas21df54asdf12asdf54asd2fasdf4a2s0df")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://flask_user:password@localhost:5433/flask_app"
