from todolist import app, db
from todolist.models import Todo
from flask import render_template, request, redirect, url_for
from datetime import date


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_item = request.form.get('newitem')
        db.session.add(Todo(item = new_item, category='Todo'))
        db.session.commit()

        return redirect(url_for('home'))
    else:
        items = Todo.query.filter_by(category='Todo').all()
        if len(items) < 1:
            db.session.add(Todo(item = 'Add a new Item +', category='Todo'))
            db.session.add(Todo(item = 'Edit an Item ------------------->', category='Todo'))
            db.session.add(Todo(item = '<-------- Complete an Item', category='Todo'))
            db.session.add(Todo(item = 'View a custom list. Hint: Add a "/" plus "the name of a list" in the URL bar. Example: /shopping', category='Todo'))
            db.session.commit()

        return render_template('home.html', items = Todo.query.filter_by(category='Todo').all(), title='Home', today=date.today())

@app.route('/<category>', methods=['GET', 'POST'])
def custom_list(category):
    if request.method == 'POST':
        new_item = request.form.get('newitem')
        item_category = request.form.get('category')

        db.session.add(Todo(item=new_item, category=item_category))
        db.session.commit()

        return redirect(url_for('custom_list', category=item_category))
    else:
        category = category.capitalize()
        item_list = Todo.query.filter_by(category=category).all()

        if len(item_list) < 1:
            db.session.add(Todo(item = 'Add a new Item +', category=category))
            db.session.add(Todo(item = 'Edit an Item ------------------->', category=category))
            db.session.add(Todo(item = '<-------- Complete an Item', category=category))
            db.session.commit()

        return render_template('custom_list.html', title=category, category=category, today=date.today(), items=Todo.query.filter_by(category=category).all())

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        item_id = request.form.get('item-id')
        item = Todo.query.filter_by(id=item_id).first()
        item_category = item.category
        Todo.query.filter_by(id=item_id).delete()
        db.session.commit()

        if item_category != 'Todo':
            return redirect(url_for('custom_list', category=item_category))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        value = Todo.query.filter_by(id=id).first()
        return render_template('edit.html', value=value, title='Edit', today = date.today())
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

        if item.category != 'Todo':
            return redirect(url_for('custom_list', category=item.category))
        else:
            return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))