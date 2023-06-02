from flask import request, redirect, url_for, render_template, flash, session
from flask_salary import app
from flask_salary.lib.culc_salary import get_breakdown

@app.route('/')
def show_home():
    return render_template('index.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        if request.form['salary'] == "":
            flash('給与が未入力です。入力してください。')
            return render_template('index.html',form_value=request.form['salary'])
        
        input_salary = int(request.form['salary'])

        MAX_DIGIT = 10
        MAX_SALARY = 10 ** (MAX_DIGIT-1) -1
        if input_salary > MAX_SALARY:
            max_digit_str = "{:,}".format(MAX_SALARY)
            flash(f'給与には最大{max_digit_str}まで入力可能です。')
            return render_template('index.html', form_value=request.form['salary'])
        elif input_salary < 0:
            flash('給与にはマイナスの値は入力できません。')
            return render_template('index.html', form_value=request.form['salary'])

        culc_pay_amount, culc_tax = get_breakdown(input_salary)

        salary_str = "{:,}".format(input_salary)
        pay_str = "{:,}".format(culc_pay_amount)
        tax_str = "{:,}".format(culc_tax)

        return render_template('output.html',salary=salary_str, pay_amount=pay_str, tax=tax_str)
    return render_template('index.html', "")

