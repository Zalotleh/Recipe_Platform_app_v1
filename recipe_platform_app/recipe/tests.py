import requests
from django.test import TestCase


# Create your tests here.

class TestAboutPage(TestCase):
    def test_about_page_decoding(self):
        response = self.client.get('/category_list/')
        self.assertEquals(response.status_code, 200)


class TestAPI(TestCase):
    def test_get_recipe_video_from_youtube(self):
        response = requests.get(
            'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=recipe&key=AIzaSyAl6LD_K0bgMe2N0DsPDgWtd7oDx-P8gv4'
        )
        self.assertEquals(response.status_code, 200)
