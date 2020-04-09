from models import db

class GroupTypeModel(db.Model):
    __tablename__ = 'GroupType'
    id_type = db.Column(db.Intger, primary_key=True)
    name = db.Column(db.String(30), nullable=False)