import json
from repositories import GroupTypeRepository 


def addGroupType(groupTypeData):
    newGroupType = {
        'name' : groupTypeData['name']
    }
    GroupTypeRepository.addInstance(**newGroupType)
    return json.dumps("Added"), 200


def getAllGroupTypes():
    groupTypes = GroupTypeRepository.getAll()
    allGroupTypes = []
    for group_type in groupTypes:
        newGroupType = {
            "id_type": group_type.id_type,
            "name": group_type.name
        }

        allGroupTypes.append(newGroupType)
    return json.dumps(allGroupTypes), 200


def deleteGroupTypeById(id):
    GroupTypeRepository.deleteInstance(id)
    return json.dumps("Deleted"), 200

def updateGroupTypeById(id, groupTypeData):
    updateFields = {
        'name' : groupTypeData['name']
    }
    GroupTypeRepository.editTnstance(id, **updateFields)

    return json.dumps("Edited"), 200

def getGroupTypeById(id):
    try:
        groupType = GroupTypeRepository.getInstance(id)
    except(IndexError):
        return json.dumps({
            "message" : "Group Doesn't exist",
            "code" : 404
            }), 404
        
    groupTypeDict = {
        "id_type": groupType.id_type,
        "name": groupType.name
    }
    return json.dumps(groupTypeDict), 200