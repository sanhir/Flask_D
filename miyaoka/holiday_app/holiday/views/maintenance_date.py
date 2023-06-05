from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
import datetime
from holiday.models.mst_holiday import Entry
# from flask_blog.views.views import login_required

@app.route('/')
# @login_required
def show_entries():
    entries = Entry.query.all()
    print(entries)
    return render_template('list.html', entries=entries)
    # return render_template('input.html')


@app.route('/entries', methods=['POST'])
# @login_required
def add_entry():
    value = request.form['button']
    # print(type(request.form['date']))INSERT INTO holiday (holi_date, holi_text)
    entry = Entry(
    holi_date=request.form['date'],
    holi_text=request.form['text']
    )
    entry.date = datetime.datetime.strptime(entry.date,'%Y-%m-%d')
    print(type(entry.date))
    print(type(entry.text))
    if value == "add":
        db.session.merge(holi_date = entry.date, holi_text = entry.text)
        db.session.commit()
        # entries = Entry.query.order_by(Entry.holi_date.desc()).all()
        # print(entries)
        flash('新しく祝日が登録されました')
        return redirect(url_for('show_entries'))
    elif value == "delete":
          return delete_entry(entry)
    elif value == 'show':
          return render_template('list.html')



# @app.route('/entries/new', methods=['GET'])
# # @login_required
# def new_entry():
#     return render_template('entries/new.html')

# @app.route('/entries/<int:id>', methods=['GET'])
# # @login_required
# def show_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/show.html', entry=entry)


# @app.route('/entries/<int:id>/edit', methods=['GET'])
# # @login_required
# def edit_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/edit.html', entry=entry)


@app.route('/<int:id>/update', methods=['POST'])
# @login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.date = request.form['date']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('祝日が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/<int:id>/delete', methods=['POST'])
# @login_required
def delete_entry(entry):
    # entry = Entry.query.get(date)
    # db.session.delete(entry)
    # db.session.commit()
    flash('祝日が削除されました')
    return render_template('result.html',entry=entry)
