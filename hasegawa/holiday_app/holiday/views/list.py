from flask import   render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route("/")
def show_holidaylist():
    holidaylist = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template("templates/list.html", holidaylist= holidaylist)

