import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", 
        "postgresql://flask_user:password@localhost:5433/flask_app"
    )


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]  # Required on Render
