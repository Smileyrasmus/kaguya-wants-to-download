from model.Group import Group

class GroupLogic:
    def create_group(self, id: int, name: str) -> Group:
        return Group(id, name)