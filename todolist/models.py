from todolist import db

class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String, nullable=False)

db.create_all()