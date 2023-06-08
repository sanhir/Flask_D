from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday

@app.route("/result", methods=["GET", "POST"])
def result():
    return render_template("result.html")

@app.route("/result/new_or_update", methods=["GET", "POST"])
def new_or_update():
    if len(request.form['date']) == 0:
        flash(' 新規登録更新失敗：祝日・日付が未入力です。カレンダーから日付を入力してください')
        return redirect(url_for('input'))
    elif len(request.form['text']) == 0:
        flash('新規登録更新失敗：祝日・テキストが未入力です。1~20文字で入力してください')
        return redirect(url_for('input'))
    elif len(request.form['text']) > 20:
        flash('新規登録更新失敗：祝日・テキストが20文字を超えています。1~20文字で入力してください')
        return redirect(url_for('input'))

    holi = Holiday.query.filter_by(holi_date=request.form['date']).first()
    if holi == None:
        holiday = Holiday(
            holi_date = request.form['date'],
            holi_text = request.form['text']
        )
        db.session.merge(holiday)
        db.session.commit()
        return render_template("result.html", holi_date=request.form['date'], holi_text=request.form['text'], flag='new')
    else:
        holi.holi_text = request.form['text']
        db.session.commit()
        return render_template("result.html", holi_date=request.form['date'], holi_text=request.form['text'], flag='update')

@app.route("/result/delete", methods=["GET", "POST"])
def delete():
    if len(request.form['date']) == 0:
        flash('削除失敗：祝日・日付が未入力です。カレンダーから日付を入力してください')
        return redirect(url_for('input'))
    holi = Holiday.query.filter_by(holi_date=request.form['date']).first()
    if holi != None:
        db.session.delete(holi)
        db.session.commit()
        return render_template("result.html", holi_date=holi.holi_date, holi_text=holi.holi_text, flag='delete')
    else:
        flash('削除失敗：登録されていない日付です')
        return redirect(url_for('input'))