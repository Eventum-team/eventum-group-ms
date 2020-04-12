from models import db


class GroupModel(db.Model):
    __tablename__ = 'Group'
    id_group = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.Integer, db.ForeignKey('GroupType.id_type'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.now(), server_default=db.func.now())
    contact_number = db.Column(db.String(15), nullable=True)
    status = db.Column(db.String(20), nullable=False)
