from resources import app
from services import GroupServices
from flask import request



@app.route('/groups', methods=['GET'])
def getAllGroups():
    return GroupServices.getAllGroups()

@app.route('/groups', methods=['POST'])
def addGroup():
    data = request.get_json()
    return GroupServices.addGroup(data)

@app.route('/groups/<id_group>', methods=['DELETE'])
def removeGroup(id_group):
    return GroupServices.deleteGroupById(id=id_group)
    
@app.route('/groups/<id_group>', methods=['PUT'])
def editGroup(id_group):
    data = request.get_json()
    return GroupServices.updateGroupById(id=id_group, groupData=data)

@app.route('/groups/<id_group>', methods=['GET'])
def getGroupById(id_group):
    return GroupServices.getGroupById(id_group)

@app.route('/groups/filter', methods=['GET'])
def filter():
    name = request.args.get('name')
    id_type = request.args.get('id_type')   

    if name is not None and id_type is not None:
        return GroupServices.getGroupsByNameAndTopicId(name, id_type)
    elif name is not None:
        return GroupServices.getGroupsByName(name)
    elif id_type is not None:
        return GroupServices.getGroupsByTopicId(id_type)
