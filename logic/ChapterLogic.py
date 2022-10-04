from functools import cache
from model.Chapter import Chapter
from model.Group import Group

class ChapterLogic:   
    def create_chapter(self,
        chapter_string: str,
        chapter_data: dict,
        group: Group
    ) -> Chapter:
        chapter = Chapter()
        chapter_string_array = chapter_string.split('.')
        
        chapter.title = chapter_data['title']
        chapter.volume = chapter_data['volume']
        chapter.number = int(chapter_string_array[0])
        chapter.extra_number = int(chapter_string_array[1]) if len(chapter_string_array) > 1 else None
        chapter.string = chapter_string
        chapter.group = group

        return chapter