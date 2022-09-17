from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from PIL import Image
from .constants import PRODUCTS_CATEGORIES_CHOICES


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ("name",)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])


class Products(models.Model):
    # category = models.CharField(max_length=30, null=True, blank=True, default="Other",
    #                             choices=PRODUCTS_CATEGORIES_CHOICES)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(default="mountain.jpg", upload_to='products-pics', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        index_together = ('id', 'slug')

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])

    # # in case we don't have an image for one product we will not get an error.
    # # if there is no image uploaded we will get an empty string url.
    # # @property decorator which let us access this as an attribute not as a method
    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url = ''
        return url
