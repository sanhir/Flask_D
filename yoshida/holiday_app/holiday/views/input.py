from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

@app.route("/", methods=["GET", "POST"])
def input():
    return render_template("input.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))