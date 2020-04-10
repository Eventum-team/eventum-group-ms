from models import db
from sqlalchemy.orm import relationship

class GroupTypeModel(db.Model):
    __tablename__ = 'GroupType'
    id_type = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    groups = relationship('GroupModel')