from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

def model_exists(model_class):
    engine = db.get_engine()
    return model_class.metadata.tables[model_class.__tablename__].exists(engine)

@app.route('/list')
def list_holiday():
    if not model_exists(Holiday):
        flash('祝日マスタが存在しません')
        redirect(url_for('input'))
    
    result = Holiday.query.all()
    if not result:
        flash('祝日マスタが登録されていません')
    print(result)
    

    return render_template('list.html', holiday_list = result)