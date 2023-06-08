from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_blog import app, db
from flask_blog.models.entries import Entry, Ojisan
from flask_blog.views.views import login_required
import random

entry = Blueprint('entry', __name__)

@entry.route("/")
@login_required
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("entries/index.html", entries=entries)

@entry.route('/entries', methods=['POST'])
@login_required
def add_entry():
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash("新しく記事が作成されました")
    return redirect(url_for('entry.show_entries'))

@entry.route('/entries/new', methods = ['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html', ojisan = 0)

@entry.route('/entries/<int:id>', methods = ['GET'])
@login_required
def show_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)

@entry.route('/entries/<int:id>/edit', methods = ['GET'])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

@entry.route('/entries/<int:id>/update', methods = ['POST'])
@login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('entry.show_entries'))

@entry.route('/entries/<int:id>/delete', methods = ['POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash("投稿が削除されました")
    return redirect(url_for('entry.show_entries'))

@entry.route('/entries/generate_ojisan', methods = ['POST','GET'])
@login_required
def generate_ojisan():
    oji_count = Ojisan.query.count()
    if oji_count == 0:
        flash('おじさん構文が登録されていません')
        return render_template('entries/new.html', ojisan=0)
    else:
        rand_num = random.randint(1, oji_count)
        ojisan = Ojisan.query.get(rand_num)
        name = request.form.get('name')
        # print(name)
        oji_text = ojisan.text.replace('name', name)
        # print(ojisan)
        return render_template('entries/new.html', oji_text=oji_text)

@entry.route('/entries/show_ojisan', methods = ['POST','GET'])
@login_required
def show_ojisan():
    ojisan = Ojisan.query.order_by(Ojisan.id.desc()).all()
    return render_template('entries/ojisan.html', ojisan=ojisan)

@entry.route('/entries/add_ojisan', methods=['POST'])
@login_required
def add_ojisan():
    ojisan = Ojisan(
        text = request.form['text']
    )
    db.session.add(ojisan)
    db.session.commit()
    flash("新しく構文が登録されました")
    return redirect(url_for('entry.show_entries'))

@entry.route('/entries/new_ojisan', methods = ['GET'])
@login_required
def new_ojisan():
    return render_template('entries/new_ojisan.html')


@entry.route('/entries/delete_ojisan/<id>', methods = ['POST','GET'])
@login_required
def delete_ojisan(id):
    print(id)
    ojisan = Ojisan.query.get(id)
    db.session.delete(ojisan)
    db.session.commit()
    flash("構文が削除されました")
    return redirect(url_for('entry.show_ojisan'))