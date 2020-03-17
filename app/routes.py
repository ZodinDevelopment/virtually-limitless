from datetime import datetime
from flask import flash, render_template, redirect, url_for, request
from app import app

@app.route('/')
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
