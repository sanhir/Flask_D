from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=['GET','POST'])


def input():
    input_num = session.get('input_num')
    return render_template('input.html', salary = ":,".format(input_num))

@app.route('/output',methods=['GET','POST'])
def output():
    session["input_num"] = ""
    salary = request.form["salary"]
    

    if salary == "":
        flash("給与が未入力です。入力してください")
        return redirect(url_for("input"))
    #給与から税額を計算
    

    elif len(str(salary)) >= 11:
        flash("給与には最大9,999,999,999まで入力可能です。") 
        return redirect(url_for("input"))

    
    elif int(salary) < 0:
        flash("給与にはマイナスの値は入力できません。")
        return redirect(url_for("input"))

    salary = int(salary)

    if salary >= 1000000:
        tax = 100000 + (salary-1000000) * 0.2
    else:
        tax = salary * 0.1
    #税額を四捨五入

    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    #支給額を計算
    after_tax_pay = salary - tax
    return render_template("output.html", salary=salary, tax=tax, after_tax_pay=after_tax_pay)
