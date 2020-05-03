from todolist import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    category = db.Column(db.String)

db.create_all()