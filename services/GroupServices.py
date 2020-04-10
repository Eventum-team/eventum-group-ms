from repositories import GroupRepository 


def addGroup(**kwargs):
    GroupRepository.add_instance(**kwargs)


def getAllGroups():
    groups = GroupRepository.get_all()
    all_groups = []
    for group in groups:
        new_group = {
            "id": group.id,
            "name": group.name
        }

        all_groups.append(new_group)
    
    return all_groups


def deleteGroupById(id):
    GroupRepository.delete_instance(id)

def updateGroupById(id, **kwargs):
    GroupRepository.edit_instance(id, **kwargs)