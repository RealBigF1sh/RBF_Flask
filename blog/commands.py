import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    from blog.models import User

    db.create_all(app=app)


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='kz@gb.ru', password=generate_password_hash('testtest'))
        )
        db.session.commit()