import json
from repositories import GroupTypeRepository 
from werkzeug.exceptions import NotFound, BadRequest


def addGroupType(groupTypeData):
    try:
        newGroupType = {
            'name' : groupTypeData['name']
        }
    except(KeyError):
        raise BadRequest("json keys in body are not correct")

    GroupTypeRepository.addInstance(**newGroupType)
    return json.dumps("Created"), 201


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
    if not id.isdecimal():
        raise BadRequest("id_type must be an integer")

    GroupTypeRepository.deleteInstance(id)
    return json.dumps("Deleted"), 200

def updateGroupTypeById(id, groupTypeData):
    if not id.isdecimal():
        raise BadRequest("id_type must be an integer")

    try:
        updateFields = {
            'name' : groupTypeData['name']
        }
    except(KeyError):
        raise BadRequest("json keys in body are not correct")
        

    try:
        GroupTypeRepository.editTnstance(id, **updateFields)
    except(IndexError):
        raise NotFound(description="Group Type doesn't exist")

    return json.dumps("Edited"), 200

def getGroupTypeById(id):
    if not id.isdecimal():
        raise BadRequest("id_type must be an integer")

    try:
        groupType = GroupTypeRepository.getInstance(id)
    except(IndexError):
        raise NotFound(description="Group Type doesn't exist")
        
    groupTypeDict = {
        "id_type": groupType.id_type,
        "name": groupType.name
    }
    return json.dumps(groupTypeDict), 200

