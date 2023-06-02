from flask import request, redirect, url_for, render_template, flash, session
from flask_calc import app
from decimal import Decimal, ROUND_HALF_UP

@app.route("/")
def show_entries():
    return render_template("entries/index.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    salary = request.form["salary"]
    if salary == "":
        flash("給与が未入力です。入力してください。")
        return redirect(url_for("show_entries"))
    elif len(salary) > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
        return redirect(url_for("show_entries"))
    else:
        salary = int(request.form["salary"])
        if salary < 0:
            flash("給与にはマイナスの値は入力できません。")
            return redirect(url_for("show_entries"))

        #給与から税額を計算
        if salary >= 1000000:
            tax = 100000 + (salary-1000000) * 0.2
        else:
            tax = salary * 0.1

        #税額を四捨五入
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

        #支給額を計算
        after_tax_pay = salary - tax
        return render_template("output.html", salary=salary, tax=tax, after_tax_pay=after_tax_pay)