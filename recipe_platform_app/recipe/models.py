from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        default='mountain.jpg',
        upload_to='category_images',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('recipe_list')

    @property
    # in case we don't have an image for one product we will not get an error.
    # if there is no image uploaded we will get an empty string url.
    # @property decorator which let us access this as an attribute not as a method
    def imageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url


choices = Category.objects.all().values_list('name', 'name')

recipe_category_choices = []

for item in choices:
    recipe_category_choices.append(item)


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=500)
    number_of_portions = models.CharField(max_length=100)
    preparation_time = models.CharField(max_length=30)
    total_time = models.CharField(max_length=30)
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='videos/', blank=True)
    likes = models.ManyToManyField(User, related_name='recipe_page', blank=True)
    category = models.CharField(max_length=30, null=True, blank=True, default="Other",
                                choices=recipe_category_choices
                                )
    external_video = EmbedVideoField(verbose_name="My online video",
                                     help_text="Your recipe video", blank=True
                                     )

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["pk"]


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="comments",
                               on_delete=models.CASCADE)
    commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.recipe.title}, {self.commenter_name}'
