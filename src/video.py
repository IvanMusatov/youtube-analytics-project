import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = build('youtube', 'v3', developerKey=os.environ['API_KEY'])
        try:
            video_data = youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()['items']
            if video_data:
                video_data = video_data[0]
                self.title = video_data['snippet']['title']
                self.url = f"https://www.youtube.com/watch?v={self.video_id}"
                self.views = int(video_data['statistics']['viewCount'])
                self.like_count = int(video_data['statistics']['likeCount'])
            else:
                self.title = None
                self.url = None
                self.views = None
                self.like_count = None
        except HttpError:
            self.title = None
            self.url = None
            self.views = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
