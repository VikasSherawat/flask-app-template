from flask import Blueprint, render_template, redirect, session, url_for, request, flash
from model import User
from forms import SignUpForm, LoginForm
from flask_login import login_required, login_user, current_user


pages = Blueprint('pages', __name__,template_folder='templates')

@pages.route("/")
@login_required
def home():
    return render_template("home.html")

@pages.route("/register", methods = ["GET","POST"])
def register():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(email=form.email.data, password=form.password.data)
        user.save()
        flash('Thanks for registering')
        return redirect(url_for('pages.home'))
    return render_template('register.html', form=form)


@pages.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('pages.login'))

        if user.is_correct_password(form.password.data):
            login_user(user)
            return redirect(url_for('pages.home'))
        else:
            return redirect(url_for('pages.login'))

    return render_template('login.html', form=form)
