from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def input():
    if "date" not in session:
        session["date"] = ""
    if "text" not in session:
        session["text"] = ""
    return render_template('input.html')


@app.route('/holidays/update', methods=['POST'])
def process_input():
    if ("holiday" not  in request.form ) or (request.form["holiday"] == ""):
        session["holiday"] = ""
    else:
        session["holiday"] = request.form["holiday"]
    if ("holiday_text" not  in request.form ) or (request.form["holiday_text"] == ""):
        session["holiday_text"] = ""
    else:
        session["holiday_text"] = request.form["holiday_text"]

    if request.form["button"] == "insert_update":
        return add_holiday()
    elif request.form["button"] == "delete":
        return delete_holiday()
    else:
        return redirect(url_for('input'))

def add_holiday():
    # 入力のバリデーション
    if session["holiday"] == "" or session["holiday_text"] == "":
        if session["holiday"] == "":
            flash("日付を入力してください")

        if session["holiday_text"] == "":
            flash("テキストを入力してください")
            
        return redirect(url_for('input'))

    holiday =  Holiday.query.get(session["holiday"])
    
    # 祝日マスタに存在しない場合、新規登録
    if not holiday:
        holiday = Holiday(
            holi_date = session["holiday"] ,
            holi_text = session["holiday_text"]
        )
        db.session().add(holiday)
        db.session().commit()
        # flash(f"{session['date']}は、祝日マスタに登録されていません")
        session["info_msg"] = f"{session['holiday'] }（{session['holiday_text']}）が登録されました。"
        return redirect(url_for('show_result'))
    # 祝日マスタに存在する場合、更新
    else:
        holiday = Holiday(
            holi_date = session["holiday"] ,
            holi_text = session["holiday_text"]
        )
        db.session().merge(holiday)
        db.session().commit()

        session["info_msg"] = f"{session['holiday'] }は「{session['holiday_text']}」に更新されました。"
        return redirect(url_for('show_result'))
    
def delete_holiday():
    print(request.form)
     # 入力のバリデーション
    if session["holiday"] == "":
        flash("日付を入力してください")
        return redirect(url_for('input'))

    holiday =  Holiday.query.get(session["holiday"])

    if not holiday:
        flash(f"{session['holiday']}は、祝日マスタに登録されていません")
        return redirect(url_for('input'))
    
    db.session.delete(holiday)
    db.session.commit()

    session["info_msg"] = f"{holiday.holi_date}（{holiday.holi_text}）は、削除されました"
    return redirect(url_for('show_result'))
