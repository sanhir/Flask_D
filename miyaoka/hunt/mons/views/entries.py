from flask import request, redirect, url_for, render_template, flash, session
from mons import app
from mons import db
from mons.models.entries import Entry
from mons.models.entries import Skill
# from flask_blog.views.views import login_required

@app.route('/')
def show_entries():
    return render_template('input.html')


@app.route('/entries', methods=['POST'])
# @login_required
def add_entry():
    value = request.form['button']
    if value == 'add_skill':
        return add_skills(request.form['skill_name'],int(request.form['skill_point']))
    if value=='show':
        s_en = Entry.query.all()
        res_point=[]
        j=0
        for i in s_en:
            res_point.append(calc_point(i)) 
            j+=1
        print(res_point[0])
        return render_template('list.html', entries = s_en,value=res_point)
    if value=='manager':
        return render_template('plus_skill.html')
    if value=='del_skill':
        return del_skill(request.form['del_skill'])
    entry = Entry(
            equip=request.form['equip'],
            srot=int(request.form['srott']),
            skill=request.form['skill'],
            rarity=int(request.form['rarity'])
            )
    if value == "add":
        return update_entry(entry)
        # db.session.merge(entry)
        # db.session.commit()
        # # flash('新しく祝日が登録されました')
        # return render_template('result.html',entry = entry, value = '追加')
    #削除処理
    elif value == "delete":
        return delete_entry(entry,request.form['del_id'])
    #一覧表示処理
    elif value == 'show':
        #   entries = Entry.query.order_by(Entry.holi_date.desc()).all()
        res_point = calc_point(entry)
        print(res_point)
        s_en = Entry.query.all()
        return render_template('list.html', entries = s_en,value=res_point)
    elif value == 'manager':
        return render_template('plus_skill.html')
    db.session.add(entry)
    db.session.commit()
    flash('新しく装備が追加されました')
    return redirect(url_for('show_entries'))

def add_skills(name,point):
    print("oooiiiii")
    skill_point = Skill(
        skill=name,
        point=point
    )
    print("skilldesuwa")
    db.session.add(skill_point)
    db.session.commit()
    return redirect(url_for('show_entries'))

def calc_point(entry):
    skill = entry.skill
    skill_list = skill.split('/')
    print(skill_list)
    sum_point = 0
    i=0
    for i in range(0,len(skill_list)):
        sp_skill = skill_list[i*2]
        db_point = Skill.query.get(sp_skill)
        sum_point = sum_point + int(db_point.point) * int(skill_list[i*2 + 1])
        if i+1 >= len(skill_list)/2:
            break
    return entry.rarity*2 - sum_point




#追加、更新処理
def update_entry(entry):
    al_res = Entry.query.get(entry.id)
    db.session.merge(entry)
    db.session.commit()
    if al_res == None:
        flash('新しく祝日が登録されました')
        return render_template('result.html',entry = entry, value = '登録')
    else:
        flash('祝日が更新されました')
        return render_template('result.html',entry=entry,value = '更新')

#削除処理
@app.route('/<int:id>/delete', methods=['POST'])
def delete_entry(entry,id):
    entry_id= Entry.query.get(id)
    if entry_id == None:
         flash('登録されていません')
         return redirect(url_for('show_entries'))
    db.session.delete(entry_id)
    db.session.commit()
    flash('削除されました')
    return render_template('result.html',entry=entry_id,value = '削除')


def del_skill(skill_name):
    entry_id= Skill.query.get(skill_name)
    if entry_id == None:
         flash('登録されていません')
         return redirect(url_for('show_entries'))
    db.session.delete(entry_id)
    db.session.commit()
    flash('削除されました')
    return render_template('result.html',entry=entry_id,value = '削除')