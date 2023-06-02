from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_blog import db

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html',entries=entries)



@app.route('/entries',methods=['POST'])
def add_entry():
    # ログインいていなければログインフォームへリダイレクト
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # ログインしていればモデルインスタンスを生成
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    # データベースに保存
    db.session.add(entry)
    # データベースに書き込み
    db.session.commit()
    flash('新しい記事が作成されました')
    return redirect(url_for('shows_entries'))

@app.route('/entries/new',methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')