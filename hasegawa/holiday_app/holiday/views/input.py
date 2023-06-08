from flask import   render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route("/")
def show_input():
    return render_template("input.html")
