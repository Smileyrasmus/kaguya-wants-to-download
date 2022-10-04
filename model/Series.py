from model.Chapter import Chapter
from model.Group import Group

class Series:
    def __init__(self) -> None:
        self.title: str = None
        self.slug: str = None
        self.groups: list[Group] = None
        self.chapters: list[Chapter] = None