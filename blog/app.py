from flask import Flask
from combojsonapi.spec import ApiSpecPlugin
from json import loads
from os import getenv, path
from blog import commands, admin
from blog.models import User
from blog.extensions import db, login_manager, migrate, csrf, ad, api
from blog.admin.route import register_views
from blog.art.views import article
from blog.user.views import user
from blog.index.views import index
from blog.auth.views import auth
from blog.author.views import author


CONFIG_PATH = getenv("CONFIG_PATH", path.join("..\config.json"))

VIEWS = [
    index,
    user,
    article,
    auth,
    author,
    ]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_api_routes()
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    ad.init_app(app)
    api.plugins = [
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
            }
        ),
    ]
    api.init_app(app)


    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_api_routes():
    from blog.api.tag import TagList
    from blog.api.tag import TagDetail

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
    register_views()
    

def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_init_tags)