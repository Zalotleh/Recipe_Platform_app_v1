from django.contrib.auth.models import User
from django.db import models
from PIL import Image

from .constants import COUNTRIES_CHOICES


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    pinterest_url = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin = models.CharField(max_length=30, null=True, blank=True, default="CV", choices=COUNTRIES_CHOICES)
    biography = models.TextField()
    avatar = models.ImageField(default="default.png", upload_to='profile-pics')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
