from models.GroupModel import GroupModel
from models import db


def getAll():
    return GroupModel.query.all()


def addInstance(**kwargs):
    instance = GroupModel(**kwargs)

    db.session.add(instance)
    db.session.commit()


def deleteInstance(id):
    GroupModel.query.filter_by(id_group=id).delete()
    db.session.commit()


def editInstance(id, **kwargs):
    instance = GroupModel.query.filter_by(id_group=id).all()[0]
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    db.session.commit()
