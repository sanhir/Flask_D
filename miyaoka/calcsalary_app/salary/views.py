from flask import request, redirect, url_for,render_template,flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def logout():
    if request.form['salary'] == "":
        flash('おい、給料入れろよ')
        return redirect(url_for('show_entries'))
    else:
        if len(request.form['salary']) > 10:
            flash('給料高すぎ')
            return redirect(url_for('show_entries'))
        salary = int(request.form['salary'])
        if salary < 0:
            flash('給料はもらうもの')
            return redirect(url_for('show_entries'))
        
        if salary >= 1000000:
            tax = 100000 + (salary-1000000) * 0.2
        else:
            tax = salary * 0.1
            #税額を四捨五入
            tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        
        #支給額を計算
        after_tax_pay = salary - tax

        return render_template("output.html", salary=salary, tax=tax, after_tax_pay=after_tax_pay)