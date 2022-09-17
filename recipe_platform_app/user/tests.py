from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile


# Create your tests here.

class ProfileTestCase(TestCase):

    def setUpTestData(cls):
        user = User.objects.create_user("user", "1976337@qq.com", "hqiwhdiui!11")
        Profile.objects.create(user=user,
                               website_url="www.facebook.org",
                               facebook_url="www.facebook.come",
                               twitter_url="twitter.com",
                               instagram_url="instagram.com",
                               pinterest_url="pinterest.com",
                               country_of_origin="CV",
                               biography="I am a great persosn",
                               avatar="recipe_platform_app/recipe_platform_app/media/profile-pics/test_profile.jpg")

    def test_image_is_saved_in_correct_size(self):
        profile = Profile.objects.get(id=1)
        image_size = profile.avatar.size
        self.assertEqual(image_size, (300, 300))
