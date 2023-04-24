from flask import Flask
from json import loads
from os import getenv, path
from blog import commands
from blog.models import User
from blog.extensions import db, login_manager, migrate
from blog.art.views import article
from blog.user.views import user
from blog.index.views import index
from blog.auth.views import auth


CONFIG_PATH = getenv("CONFIG_PATH", path.join("..\config.json"))

VIEWS = [
    index,
    user,
    article,
    auth,
    ]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)

def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)