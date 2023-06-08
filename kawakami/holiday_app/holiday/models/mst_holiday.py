from  holiday import db

# 祝日というモデルの定義
# モデルにHolidayという名前をつける
class Holiday(db.Model):
    __tablename__ = "holiday"
    holi_date = db.Column("holi_date",db.Date,primary_key = True)
    holi_text = db.Column("holi_text",db.String(20))

    # 記事が作成された時の標準動作を定義
    def __init__(self,holi_date=None,holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text
        
    # 記事モデルが参照されたときのコンソールでの出力形式を記載
    def __repr__ (self):
        return '< Holiday holi_date:{} holi_text:{} >'.format(self.holi_date,self.holi_text)
