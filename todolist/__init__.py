from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DATABASE_URL'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from todolist import routes