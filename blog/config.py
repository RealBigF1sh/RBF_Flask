import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('flask_venv', default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True