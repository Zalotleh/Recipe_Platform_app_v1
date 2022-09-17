import os

import googleapiclient.discovery
import googleapiclient.errors
from django.conf import settings

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


class YouTube:

    def __init__(self, *args, **kwargs):
        self.vid_id = kwargs.get("vid_id")

        self.api_service_name = settings.API_SERVICE_NAME
        self.api_version = settings.API_VERSION
        self.developer_key = settings.GOOGLE_API_KEY

        self.youtube = googleapiclient.discovery.build(
            self.api_service_name,
            self.api_version,
            developerKey=self.developer_key
        )

    def get_video(self):
        request = self.youtube.search().list(
            part="snippet",
            maxResults=25,
            order="date",
            q="recipe"
        )
        response = request.execute()

        item = response["items"][0]

        vid_data = {
            "id": item["id"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
        }

        return vid_data
