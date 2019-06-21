
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('shop:category_products', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    image = models.ImageField(blank=True, upload_to="shop")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(City, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ('-added',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f"ARGS: {args}")
        print(f"KWARGS: {args}")
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def image_url(self):
        """
        Returns the URL of the image associated with this Object.
        If an image hasn't been uploaded yet, it returns a stock image

        :returns: str -- the image url

        """

        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/img/no_image.png'
