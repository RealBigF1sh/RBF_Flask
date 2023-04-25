from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from blog.models import User
from blog.forms.login_form import LoginForm
from blog.extensions import db

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))
    
    form = LoginForm(request.form)
    
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="user doesn't exist")
        if User.query.filter_by(password=form.password.data).count():
            return render_template("auth/login.html", form=form, error="invalid email or password")
        login_user(user)
        return redirect(url_for('.login'))
    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))