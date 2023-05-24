import os
from datetime import timedelta

from googleapiclient.discovery import build
from isodate import parse_duration


class PlayList:
    def __init__(self, playlist_id):
        api_key = os.getenv('API_KEY')
        self.id = playlist_id
        self.api = build('youtube', 'v3', developerKey=api_key)
        playlist = self.api.playlists().list(id=self.id, part='snippet').execute().get('items')[0]
        self.title = playlist['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.id}"

    @property
    def total_duration(self):
        videos = self.api.playlistItems().list(playlistId=self.id, part='contentDetails').execute().get('items')
        total_duration = timedelta()
        for video in videos:
            content_details = video.get('contentDetails')
            if 'duration' in content_details:
                duration = content_details['duration']
                parsed_duration = parse_duration(duration)
                total_duration += parsed_duration
        return total_duration

    def show_best_video(self):
        videos = self.api.playlistItems().list(playlistId=self.id, part='snippet').execute().get('items')
        best_video = max(videos, key=lambda v: int(v['snippet']['position']))
        return f"https://www.youtube.com/watch?v={best_video['snippet']['resourceId']['videoId']}"


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
duration = pl.total_duration

print(duration)
print(pl.show_best_video())