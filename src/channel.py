from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self.service = Channel.get_service()

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        if channel['items']:
            channel = channel['items'][0]
            self.title = channel['snippet']['title']
            self.description = channel['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = channel['statistics']['subscriberCount']
            self.video_count = channel['statistics']['videoCount']
            self.view_count = channel['statistics']['viewCount']

    # @property
    # def channel_id(self):
    # return self.channel_id

    def __str__(self):
        channel = self.service.channels().list(id=self.channel_id, part='snippet').execute()['items'][0]
        return f"{channel['snippet']['title']} (https://www.youtube.com/channel/{self.channel_id})"

    def __add__(self, other):
        subscribers1 = \
        self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
            'subscriberCount']
        subscribers2 = \
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount']
        return int(subscribers1) + int(subscribers2)

    def __sub__(self, other):
        subscribers1 = \
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount']
        subscribers2 = \
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount']
        return int(subscribers1) - int(subscribers2)

    def __gt__(self, other):
        subscribers1 = int(
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        subscribers2 = int(
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        return subscribers1 > subscribers2

    def __ge__(self, other):
        subscribers1 = int(
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        subscribers2 = int(
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        return subscribers1 >= subscribers2

    def __lt__(self, other):
        subscribers1 = int(
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        subscribers2 = int(
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        return subscribers1 < subscribers2

    def __le__(self, other):
        subscribers1 = int(
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        subscribers2 = int(
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        return subscribers1 <= subscribers2

    def __eq__(self, other):
        subscribers1 = int(
            self.service.channels().list(id=self.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        subscribers2 = int(
            other.service.channels().list(id=other.channel_id, part='statistics').execute()['items'][0]['statistics'][
                'subscriberCount'])
        return subscribers1 == subscribers2

    @staticmethod
    def get_service():
        """Возвращает объект для работы с API."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, file_name: str) -> None:
        """Сохраняет данные о канале в JSON-файл."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
