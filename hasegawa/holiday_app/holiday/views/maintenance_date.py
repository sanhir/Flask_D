from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from datetime import date

@app.route("/", methods=["POST"])
def show_result():
    if "holi_date" in request.form and request.form["holi_date"] != "":
        session["input_data"] = request.form["holi_date"]
        # print(session["input_data"])
        # print("aaaaaaaaaaaaaaaaaaa")
        
    else:
        flash('祝日が入力されていません。')
        return redirect(url_for('show_input'))


    if request.form["button"] == "insert_update":
        value_add_or_update = add_or_update_holiday()
        return value_add_or_update
    
    elif request.form["button"] == "delete":
        value_delete = delete_holiday()
        return value_delete

@app.route("/add_or_update", methods = ["POST"])
def add_or_update_holiday():
    if len(request.form['holi_text']) == 0:
        flash('テキストが入力されていません')  
        return redirect(url_for('show_input'))  
    elif len(request.form['holi_text']) > 20:
        flash("テキストが長すぎます。1-20文字で入力してください。")
        return redirect(url_for('show_input'))
    
    db_date = Holiday.query.filter_by(holi_date=request.form['holi_date']).first()

    if db_date == None:
        holiday = Holiday(
            holi_date = request.form['holi_date'],
            holi_text = request.form['holi_text']
        )
        db.session.merge(holiday)
        db.session.commit()
        return render_template("result.html", flag="add", holi_date = request.form["holi_date"], holi_text = request.form["holi_text"])
    else:
        db_date.holi_text = request.form['holi_text']
        db.session.commit()
        return render_template("result.html", flag="update", holi_date = request.form["holi_date"], holi_text = request.form["holi_text"])
    

@app.route("/delete", methods=["GET","POST"])
def delete_holiday():
    print(session['input_data'])
    db_date = Holiday.query.get(session['input_data'])
    
    if db_date != None:
        db.session.delete(db_date)
        db.session.commit()
        return render_template("result.html", flag="delete", holi_date = db_date.holi_date, holi_text = db_date.holi_text)
    else:
        flash("登録されていないので削除できません")
        return redirect(url_for('show_input'))
