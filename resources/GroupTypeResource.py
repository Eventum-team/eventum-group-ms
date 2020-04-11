from resources import app
from services import GroupTypeServices
from flask import request

@app.route('/group-types', methods=['GET'])
def createGroupType():
    return GroupTypeServices.getAllGroupTypes()
    

@app.route('/group-types', methods=['POST'])
def addGroupType():
    groupTypeData = request.get_json()
    return GroupTypeServices.addGroupType(groupTypeData)
    

@app.route('/group-types/<groupTypeId>', methods=['DELETE'])
def removeGroupTypeById(groupTypeId):
    return GroupTypeServices.deleteGroupTypeById(id=groupTypeId)
    


@app.route('/group-types/<groupTypeId>', methods=['PUT'])
def editGroupTypeById(groupTypeId):
    groupTypeData = request.get_json()
    return GroupTypeServices.updateGroupTypeById(id=groupTypeId, groupTypeData=groupTypeData)
    
@app.route('/group-types/<groupTypeId>', methods=['GET'])
def getGroupTypeById(groupTypeId):
    return GroupTypeServices.getGroupTypeById(groupTypeId)
