from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route("/")
def show_result():
    return render_template("templates/result.html")

@app.route("/templates", methods = ['POST'])
def add_holiday():
    holiday = Holiday(
        holi_date = request.form['holi_date'],
        holi_text = request.form['holi_text']
    )
    db.session.add(holiday)
    db.session.commit()
    flash('祝日が登録されました')
    return redirect(url_for('show_result'))

@app.route("/templates/<int:id>/update", methods = ['POST'])
def update_holiday(id):
    holiday = Holiday.query.get(id)
    holiday.holi_date = request.form['holi_date']
    holiday.holi_text = request.form['holi_text']
    db.session.merge(holiday)
    db.session.commit()
    flash('祝日が更新されました')
    return redirect(url_for('show_result'))

@app.route("/templates/<int:id>/edit", methods = ['GET'])
def edit_holiday(id):
    holiday = Holiday.query.get(id)
    return redirect(url_for('show_result'))

@app.route("/templates/<int:id>/delete", methods=['POST'])
def delete_holiday(id):
    holiday = Holiday.query.get(id)
    db.session.delete(holiday)
    db.session.commit()
    flash('祝日が削除されました')
    return redirect(url_for('show_result'))