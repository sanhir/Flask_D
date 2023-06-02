# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
# __init__.pyで作成したappをインポート
from salary import app 

# 最初にinput.htmlを表示する
@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('input.html')


# 「計算する」を押された時の処理
@app.route('/output',methods = ['GET','POST'])
def calc():
    if request.form["salary"] == "":
        flash("給与が未入力です。入力してください。")
        return redirect(url_for('home'))
    elif len(request.form["salary"]) > 10 :
        flash("給与には最大999,999,999まで入力可能です。")
        return redirect(url_for('home'))
    elif int(request.form["salary"]) < 0:
        flash("給与にはマイナスの値は入力できません。")
        return redirect(url_for('home'))

    salary = int(request.form["salary"])
    v = 1000000
    if salary <= v:
        tax = salary * 0.1
    else:
        tax = v * 0.1 + (salary - v) * 0.2
    from decimal import Decimal, ROUND_HALF_UP
    tax = int(Decimal(str(tax)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    pay = int(salary - tax)

    salary = str(salary)
    tax = str(tax)
    pay = str(pay)
    return render_template('output.html',salary = salary,tax = tax,pay = pay)


# 「戻る」を押された時の処理
@app.route('/input')
def back():
    return render_template('input.html')

