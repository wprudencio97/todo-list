from todolist import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String, nullable=False)

db.create_all()