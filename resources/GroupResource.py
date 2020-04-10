from resources import app
from services import GroupServices
import json
from flask import request

@app.route('/', methods=['GET'])
def fetch():
    all_groups = GroupServices.getAllGroups()
    return json.dumps(all_groups), 200

"""
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200
"""

@app.route('/remove/<group_id>', methods=['DELETE'])
def remove(group_id):
    GroupServices.delete_instance(id=group_id)
    return json.dumps("Deleted"), 200


"""
@app.route('/edit/<group_id>', methods=['PUT'])
def edit(group_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200
"""