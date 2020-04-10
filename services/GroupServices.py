from repositories import GroupRepository 


def addGroup(**kwargs):
    GroupRepository.add_instance(**kwargs)


def getAllGroup():
    return GroupRepository.get_all()


def deleteGroupById(id):
    GroupRepository.delete_instance(id)

def updateGroupById(id, **kwargs):
    GroupRepository.edit_instance(id, **kwargs)