from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/maintenance_date')
def show_result():
    if "info_msg" not in session or not session["info_msg"]:
        redirect(url_for('input'))
    return render_template('result.html')