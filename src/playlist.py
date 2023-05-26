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
            video_id = content_details.get('videoId')
            if video_id:
                video_data = self.api.videos().list(part='contentDetails, statistics', id=video_id).execute()
                duration = video_data["items"][0]["contentDetails"]["duration"]
                parsed_duration = parse_duration(duration)
                total_duration += parsed_duration
        return total_duration

    def show_best_video(self):
        videos = self.api.playlistItems().list(playlistId=self.id, part='snippet').execute().get('items')
        best_video = max(videos, key=lambda v: int(v['snippet']['position']))
        video_id = best_video['snippet']['resourceId']['videoId']
        return f"https://youtu.be/{video_id}"
