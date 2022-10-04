import io
import os
from zipfile import ZipFile
from Utils import Utils
from model.Chapter import Chapter
import re


class FileSystemClient:
    def __init__(self) -> None:
        # TODO: make a class decorator to ensure working dir is set correctly before any method is executed
        working_dir = f"{os.path.dirname(__file__)}\\..\\Synced_Manga"
        self.ensure_dir(working_dir)
        os.chdir(working_dir)
    
    def save_chapter(self, series_title: str, chapter: Chapter, chapter_zip_data: any) -> None:
        chapter_path = self.get_dir_for_chapter(series_title, chapter)
        with ZipFile(io.BytesIO(chapter_zip_data)) as zip_file:
            zip_file.extractall(chapter_path)

    def chapter_exists(self, series_title: str, chapter: Chapter) -> bool:
        dir_for_chapter = self.get_dir_for_chapter(series_title, chapter, False)
        dir_exists = os.path.exists(dir_for_chapter)
        dir_is_not_empty = False
        # check if dir is truly empty
        if dir_exists:
            files_in_dir = os.listdir(dir_for_chapter)
            dir_is_not_empty = len(files_in_dir) > 0
        return dir_exists and dir_is_not_empty
    
    def get_dir_for_chapter(self, series_title: str, chapter: Chapter, create_missing_dirs: bool=True) -> str:
        path_dirs = [
            series_title,
            f'Volume {Utils.format_number(chapter.volume, 2)}',
            self.get_formatted_chapter_name(chapter),
            chapter.group.name,
            ]
        # One step at a time, check if dir exists. If not, create dir.
        path = ''
        for dir in path_dirs:
            dir = self.remove_illegal_dir_characters(dir)
            path += f'{dir}\\'
            if create_missing_dirs: self.ensure_dir(path)
        return path
        
    def ensure_dir(self, dir: str) -> None:
        if not os.path.exists(dir): os.mkdir(dir)

    def get_formatted_chapter_name(self, chapter: Chapter) -> str:
        chapter_string = Utils.format_number(chapter.number)
        if chapter.extra_number:
            chapter_string += f'.{chapter.extra_number}'
        chapter_string += f' - {chapter.title}'
        return chapter_string

    def remove_illegal_dir_characters(self, dir: str) -> str:
        dir = dir.strip() # dir ending or starting with whitespace is illegal
        cleaned_dir = dir.replace(':', ';')
        cleaned_dir = re.sub(r'[#%<>&*{}?/\\$+`\'"=|:@]', '', cleaned_dir)
        return cleaned_dir