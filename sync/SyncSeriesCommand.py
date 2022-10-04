from client.FileSystemClient import FileSystemClient
from client.GuyaClient import GuyaClient
from model.Series import Series

class SyncSeriesCommand:
    def __init__(self) -> None:
        self.guya_client = GuyaClient()
        self.file_system_client = FileSystemClient()

    def execute(self, series: Series) -> None:
        print(f"Syncing '{series.title}'")
        for chapter in series.chapters:
            if not self.file_system_client.chapter_exists(series.title, chapter):
                print(f'Downloading chapter {chapter.string} by {chapter.group.name}... ', end='', flush=False)
                zip_file_data = self.guya_client.download_chapter(series.slug, chapter)
                print('Done, Saving... ', end='', flush=False)
                self.file_system_client.save_chapter(series.title, chapter, zip_file_data)
                print('Done')
        print(f"Syncing of '{series.title}' is done")