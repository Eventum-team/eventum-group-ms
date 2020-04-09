from models.GroupTypeModel import GroupTypeModel
from models import db


def get_all():
    return GroupTypeModel.query.all()


def add_instance(**kwargs):
    instance = GroupTypeModel(**kwargs)

    db.session.add(instance)
    db.session.commit()


def delete_instance(id):
    GroupTypeModel.query.filter_by(id=id).delete()
    db.session.commit()


def edit_instance(id, **kwargs):
    instance = GroupTypeModel.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    db.session.commit()