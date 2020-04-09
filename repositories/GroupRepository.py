from models.GroupModel import GroupModel
from models import db


def get_all():
    return GroupModel.query.all()


def add_instance(**kwargs):
    instance = GroupModel(**kwargs)

    db.session.add(instance)
    db.session.commit()


def delete_instance(id):
    GroupModel.query.filter_by(id=id).delete()
    db.session.commit()


def edit_instance(id, **kwargs):
    instance = GroupModel.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    db.session.commit()
