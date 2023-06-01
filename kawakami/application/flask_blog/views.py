# flaskのパッケージをインポート
from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')

# /loginのURLにリクエストがあったときのルーティング処理

@app.route('/login',methods = ['GET','Post'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            # ログイン成功後に=Trueにセット、リクエストのたびにチェックすることでログインしているかを判別することができる
            session['logged_in'] = True
            flash('ログインしました')
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    # logoutしたらsessionを削除
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect('/')
    
        