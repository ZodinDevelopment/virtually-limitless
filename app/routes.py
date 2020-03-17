from datetime import datetime
from flask import flash, render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
@login_required
def index():

    # This is a sample user for testing templates
    user = {'username': 'Toaster'}

    posts = [
        {
            "author": {"username": "admin"},
            "headline": "Good news everyone!",
            "date_time_posted": datetime.now().ctime(),
            "body": "Hey, make sure you're running the latest version of Python!"
        },
        {
            "author": {"username": "Trey"},
            "headline": "How is everyone?!",
            "date_time_posted": datetime.now().ctime(),
            "body": "Don't waste your brilliance on the streets! Come train with the Jedi!"
        }
    ]
    return render_template("index.html", title="Dashboard", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # this is like the function above but will handle more data and has a FlaskForm initialized
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
