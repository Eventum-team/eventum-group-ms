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

@app.route('/groups/<groupId>', methods=['DELETE'])
def removeGroup(groupId):
    return GroupServices.deleteGroupById(id=groupId)
    
@app.route('/groups/<groupId>', methods=['PUT'])
def editGroup(groupId):
    data = request.get_json()
    return GroupServices.updateGroupById(id=groupId, groupData=data)

@app.route('/groups/<groupId>', methods=['GET'])
def getGroupById(groupId):
    return GroupServices.getGroupById(groupId)
     
