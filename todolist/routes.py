from todolist import app, db
from todolist.models import Todo
from flask import render_template, request, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_item = request.form.get('newitem')
        db.session.add(Todo(item = new_item))
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('home.html', items = Todo.query.all(), title='Home')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        item_id = request.form.get('item-id')
        Todo.query.filter_by(id=item_id).delete()
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        value = Todo.query.filter_by(id=id).first()
        return render_template('edit.html', value=value, title='Edit')
    else:
        return redirect(url_for('home'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        item_id = request.form.get('id')
        item_content = request.form.get('item')

        item = Todo.query.filter_by(id=item_id).first()
        item.item = item_content
        db.session.commit()

        return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))