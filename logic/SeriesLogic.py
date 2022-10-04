from model.Chapter import Chapter
from model.Group import Group
from model.Series import Series
from logic.GroupLogic import GroupLogic
from logic.ChapterLogic import ChapterLogic

class SeriesLogic:
    def __init__(self) -> None:
        self.group_logic = GroupLogic()
        self.chapter_logic = ChapterLogic()
    
    def create_series(self, series_data: dict) -> Series:
        series = Series()

        series.title = series_data['title']
        series.slug = series_data['slug']
        series.groups = self.get_groups(series_data['groups'])
        series.chapters = self.get_chapters(series_data['chapters'], series.groups)

        return series

    def get_groups(self, groups_data: dict) -> list[Group]:
        groups = []
        for group_id, group_name in groups_data.items():
            groups.append(self.group_logic.create_group(group_id, group_name))
        return groups
    
    def get_chapters(self, chapters_data: dict, all_groups: list[Group]) -> list[Chapter]:
        chapters = []
        for chapter_string, chapter_data in chapters_data.items():
            # use groups from a given chapter.
            chapter_groups = [group for group in all_groups if group.id in chapter_data['groups']]
            # create one chapter for each group, so we get all fan dubs of a given chapter
            for group in chapter_groups:
                chapters.append(self.chapter_logic.create_chapter(chapter_string, chapter_data, group))
        return chapters