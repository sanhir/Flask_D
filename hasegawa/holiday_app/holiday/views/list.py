from flask import   render_template, flash, redirect, url_for
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route("/list", methods=["GET","POST"])
def show_holidaylist():
    # db_list = Holiday.query.all()
    # if db_list == None:

    #     return render_template("list.html", holidaylist= holidaylist)
    # else:    
        holidaylist = Holiday.query.order_by(Holiday.holi_date.asc()).all()
        return render_template("list.html", holidaylist= holidaylist)