
from repositories import GroupTypeRepository 


def addGroupType(**kwargs):
    GroupTypeRepository.add_instance(**kwargs)


def getAllGroupTypes():
    return GroupTypeRepository.get_all()


def deleteGroupTypeById(id):
    GroupTypeRepository.delete_instance(id)

def updateGroupTypeById(id, **kwargs):
    GroupTypeRepository.edit_instance(id, **kwargs)