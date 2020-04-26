from todolist import app
from todolist.models import todo
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')