
from repositories import GroupTypeRepository 


def addGroupType(groupTypeData):
    newGroupType = {
        'name' : groupTypeData['name']
    }
    GroupTypeRepository.addInstance(**newGroupType)


def getAllGroupTypes():
    groupTypes = GroupTypeRepository.getAll()
    allGroupTypes = []
    for group_type in groupTypes:
        newGroupType = {
            "id_type": group_type.id_type,
            "name": group_type.name
        }

        allGroupTypes.append(newGroupType)
    return allGroupTypes


def deleteGroupTypeById(id):
    GroupTypeRepository.deleteInstance(id)

def updateGroupTypeById(id, groupTypeData):
    updateFields = {
        'name' : groupTypeData['name']
    }
    GroupTypeRepository.editTnstance(id, **updateFields)