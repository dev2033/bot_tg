import json
from typing import Any, Optional, Dict

from bot.api import API


class LikeeAPI(API):

    @property
    def headers(self) -> Dict[str, Any]:
        return {'Referer': 'https://www.likee.video/'}

    @property
    def links(self):
        return ['likee.video', 'like-video.com']

    @property
    def regexp_key(self) -> str:
        return r'"video_url":'

    def _parse_data(self, script: str) -> Optional[str]:
        js = json.loads(script.split('window.data = ')[-1][:-1])
        return js.get('video_url')
