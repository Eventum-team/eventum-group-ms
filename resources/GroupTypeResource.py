from resources import app
from services import GroupTypeServices
import json
from flask import request

@app.route('/groupTypes', methods=['GET'])
def createGroupType():
    allGroupTypes = GroupTypeServices.getAllGroupTypes()
    return json.dumps(allGroupTypes), 200

@app.route('/groupTypes', methods=['POST'])
def addGroupType():
    groupTypeData = request.get_json()
    GroupTypeServices.addGroupType(groupTypeData)
    return json.dumps("Added"), 200

@app.route('/groupTypes/<groupTypeId>', methods=['DELETE'])
def removeGroupTypeById(groupTypeId):
    GroupTypeServices.deleteGroupTypeById(id=groupTypeId)
    return json.dumps("Deleted"), 200


@app.route('/groupTypes/<groupTypeId>', methods=['PUT'])
def editGroupTypeById(groupTypeId):
    groupTypeData = request.get_json()
    GroupTypeServices.updateGroupTypeById(id=groupTypeId, groupTypeData=groupTypeData)
    return json.dumps("Edited"), 200
