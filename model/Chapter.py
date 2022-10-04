from model.Group import Group

class Chapter:
    def __init__(self):
        self.title: str = None
        self.volume: int = None
        self.number:int = None
        self.extra_number:int = None
        self.string: str = None
        self.group: Group = None

    def __lt__(self, other):
        return self.formatted_chapter < other.formatted_chapter
    
    def __gt__(self, other):
        return self.formatted_chapter > other.formatted_chapter
    
    def __eq__(self, other):
        if isinstance(other, Chapter):
            return (
                self.number == other.number and
                self.extra_number == other.extra_number and
                self.group == other.group
            )
        return False
    
    def __hash__(self):
        return hash((
            'chapter_number', self.number,
            'extra_chapter_number', self.extra_number,
            'group_id', self.group.id
        ))