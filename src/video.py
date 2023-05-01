import os

from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = build('youtube', 'v3', developerKey=os.environ['API_KEY'])
        video = youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()['items'][0]['snippet']
        self.title = video['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.views = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['viewCount'])
        self.likes = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title


class PLVideo:
    def __init__(self, video_id, playlist_id):
        self.video_id = video_id
        self.playlist_id = playlist_id
        youtube = build('youtube', 'v3', developerKey=os.environ['API_KEY'])
        video = youtube.videos().list(part='snippet, statistics', id=self.video_id).execute()['items'][0]['snippet']
        self.title = video['title']
        self.url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.views = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['viewCount'])
        self.likes = int(
            youtube.videos().list(part='statistics', id=self.video_id).execute()['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.title
