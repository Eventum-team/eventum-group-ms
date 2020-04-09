from models import db


class GroupModel(db.Model):
    __tablename__ = 'Group'
    id_group = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    decription = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False)
    contact_number = db.Column(db.String(15), nullable=True)
    status = db.Column(db.String(20), nullable=False)