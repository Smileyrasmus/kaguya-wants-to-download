import io
import json
import requests
from model.Chapter import Chapter

class GuyaClient:
    def __init__(self) -> None:
        self.domain = 'https://guya.cubari.moe'

    def get_kaguya_sama_series(self) -> dict:
        return self.get_series('Kaguya-Wants-To-Be-Confessed-To')
    
    def get_we_want_to_talk_about_kaguya_series(self) -> dict:
        return self.get_series('We-Want-To-Talk-About-Kaguya')
    
    def download_chapter(self, series_slug: str, chapter: Chapter) -> any:
        content = None
        url = f'{self.domain}/api/download_chapter/{series_slug}/{chapter.string.replace(".", "-")}?group={chapter.group.id}'
        with requests.get(url) as response:
            content = response.content
        return content
    
    def get_series(self, series_slug: str) -> dict:
        content = None
        with requests.get(f'{self.domain}/api/series/{series_slug}/') as response:
            content = json.load(io.BytesIO(response.content))
        return content