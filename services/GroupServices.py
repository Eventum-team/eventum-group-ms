from repositories import GroupRepository 
import datetime
from werkzeug.exceptions import NotFound, BadRequest
import json



def addGroup(groupData):
    try:
        newGroup = {
            'id_type' : groupData['id_type'],
            'name' : groupData['name'],
            'description' : groupData['description'],
            'contact_number' : groupData['contact_number'],
            'status' : groupData['status']
        }
    except(KeyError):
        raise BadRequest("json keys in body are not correct")

    
    GroupRepository.addInstance(**newGroup)

    return json.dumps("Created"), 201


def getAllGroups():
    groups = GroupRepository.getAll()
    allGroups = formatGroupList(groups)
    return json.dumps(allGroups, default=datetimeConverter), 200


def deleteGroupById(id):
    if not id.isdecimal():
        raise BadRequest("id_group must be an integer")

    GroupRepository.deleteInstance(id)
    return json.dumps("Deleted"), 200

def updateGroupById(id, groupData):
    if not id.isdecimal():
        raise BadRequest("id_group must be an integer")

    try:
        updateFields = {
            'id_type' : groupData['id_type'],
            'name' : groupData['name'],
            'description' : groupData['description'],
            'contact_number' : groupData['contact_number'],
            'status' : groupData['status']
        }
    except(KeyError):
        raise BadRequest("json keys in body are not correct")


    GroupRepository.editInstance(id, **updateFields)
    return json.dumps("Edited"), 204


def getGroupById(id):
    if not id.isdecimal():
        raise BadRequest("id_group must be an integer")

    try:
        group = GroupRepository.getInstance(id)
    except(IndexError):
        raise NotFound(description="Group doesn't exist")

    groupDict = {
        "id_group": group.id_group,
        "id_type" : group.id_type,
        "name": group.name,
        "description" : group.description,
        "created_date" : group.created_date,
        "contact_number" : group.contact_number,
        "status" : group.status
    }
    return json.dumps(groupDict, default=datetimeConverter), 200


def getGroupsByName(name):
    groups = GroupRepository.getInstanceByName(formatSearch(name))
    selectedGroups = formatGroupList(groups)
    return json.dumps(selectedGroups, default=datetimeConverter), 200


def getGroupsByTopicId(id_type):
    if not id_type.isdecimal():
        raise BadRequest("id_type must be an integer")

    groups = GroupRepository.getInstanceByTypeId(id_type)
    selectedGroups = formatGroupList(groups)
    return json.dumps(selectedGroups, default=datetimeConverter), 200


def getGroupsByNameAndTopicId(name, id_type):
    if not id_type.isdecimal():
        raise BadRequest("id_type must be an integer")

    groups = GroupRepository.getInstanceByNameAndTypeId(formatSearch(name), id_type)
    selectedGroups = formatGroupList(groups)
    return json.dumps(selectedGroups, default=datetimeConverter), 200





###############################################
############# HELPER FUNCTIONS ################
###############################################


def formatSearch(word):
    if '*' in word or '_' in word: 
        return word.replace('_', '__')\
                    .replace('*', '%')\
                    .replace('?', '_')
    
    return '%{0}%'.format(word)

def datetimeConverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def formatGroupList(groups):
    allGroups = []
    for group in groups:
        newGroup = {
            "id_group": group.id_group,
            "id_type" : group.id_type,
            "name": group.name,
            "description" : group.description,
            "created_date" : group.created_date,
            "contact_number" : group.contact_number,
            "status" : group.status
        }
        allGroups.append(newGroup)
    return allGroups