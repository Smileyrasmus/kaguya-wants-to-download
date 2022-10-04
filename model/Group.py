class Group:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Group):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash((
            'id', self.id
        ))
