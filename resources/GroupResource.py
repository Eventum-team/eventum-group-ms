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

@app.route('/groups/<group_id>', methods=['DELETE'])
def removeGroup(group_id):
    return GroupServices.deleteGroupById(id=group_id)
    
@app.route('/groups/<group_id>', methods=['PUT'])
def editGroup(group_id):
    data = request.get_json()
    return GroupServices.updateGroupById(id=group_id, groupData=data)

@app.route('/groups/<group_id>', methods=['GET'])
def getGroupById(group_id):
    return GroupServices.getGroupById(group_id)

@app.route('/groups/name/<group_name>', methods=['GET'])
def getGroupsByName(group_name):
    return GroupServices.getGroupsByName(group_name)

@app.route('/groups/type/<type_id>', methods=['GET'])
def getGroupsByTopicId(type_id):
    return GroupServices.getGroupsByTopicId(type_id)

@app.route('/groups/name-type/<group_name>/<type_id>', methods=['GET'])
def getGroupsByNameAndTopicId(group_name, type_id):
    return GroupServices.getGroupsByNameAndTopicId(group_name, type_id)
