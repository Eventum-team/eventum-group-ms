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
    

@app.route('/group-types/<type_id>', methods=['DELETE'])
def removeGroupTypeById(type_id):
    return GroupTypeServices.deleteGroupTypeById(id=type_id)
    


@app.route('/group-types/<type_id>', methods=['PUT'])
def editGroupTypeById(type_id):
    groupTypeData = request.get_json()
    return GroupTypeServices.updateGroupTypeById(id=type_id, groupTypeData=groupTypeData)
    
@app.route('/group-types/<type_id>', methods=['GET'])
def getGroupTypeById(type_id):
    return GroupTypeServices.getGroupTypeById(type_id)
