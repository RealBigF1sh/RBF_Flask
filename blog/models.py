from flask_login import UserMixin
from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, default="", server_default="")
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(255))

    def __init__(self, email, password, is_staff):
        self.email = email
        self.password = password
        self.is_staff = is_staff