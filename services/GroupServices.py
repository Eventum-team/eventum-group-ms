from repositories import GroupRepository 
import datetime
import json


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def addGroup(groupData):
    newGroup = {
        'id_type' : groupData['id_type'],
        'name' : groupData['name'],
        'description' : groupData['description'],
        'contact_number' : groupData['contact_number'],
        'status' : groupData['status']
    }
    GroupRepository.addInstance(**newGroup)

    return json.dumps("Added"), 200


def getAllGroups():
    groups = GroupRepository.getAll()
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
    
    return json.dumps(allGroups, default=myconverter), 200


def deleteGroupById(id):
    GroupRepository.deleteInstance(id)
    return json.dumps("Deleted"), 200

def updateGroupById(id, groupData):
    updateFields = {
        'id_type' : groupData['id_type'],
        'name' : groupData['name'],
        'description' : groupData['description'],
        'contact_number' : groupData['contact_number'],
        'status' : groupData['status']
    }
    GroupRepository.editInstance(id, **updateFields)

    return json.dumps("Edited"), 200