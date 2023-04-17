import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('flask_venv', default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/blog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False