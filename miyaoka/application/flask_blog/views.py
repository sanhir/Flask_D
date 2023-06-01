from flask import request, redirect, url_for,render_template,flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
            print(request.form['username'])
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
            print(request.form['password'])
        else:
            return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect('/')