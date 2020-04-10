from models.GroupTypeModel import GroupTypeModel
from models import db


def getAll():
    return GroupTypeModel.query.all()


def addInstance(**kwargs):
    instance = GroupTypeModel(**kwargs)

    db.session.add(instance)
    db.session.commit()


def deleteInstance(id):
    GroupTypeModel.query.filter_by(id_type=id).delete()
    db.session.commit()


def editTnstance(id, **kwargs):
    instance = GroupTypeModel.query.filter_by(id_type=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    db.session.commit()