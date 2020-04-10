from resources import app
from services import GroupTypeServices
from flask import request

@app.route('/groupTypes', methods=['GET'])
def createGroupType():
    return GroupTypeServices.getAllGroupTypes()
    

@app.route('/groupTypes', methods=['POST'])
def addGroupType():
    groupTypeData = request.get_json()
    return GroupTypeServices.addGroupType(groupTypeData)
    

@app.route('/groupTypes/<groupTypeId>', methods=['DELETE'])
def removeGroupTypeById(groupTypeId):
    return GroupTypeServices.deleteGroupTypeById(id=groupTypeId)
    


@app.route('/groupTypes/<groupTypeId>', methods=['PUT'])
def editGroupTypeById(groupTypeId):
    groupTypeData = request.get_json()
    return GroupTypeServices.updateGroupTypeById(id=groupTypeId, groupTypeData=groupTypeData)
    
