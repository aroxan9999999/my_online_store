from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    fullDescription = models.TextField(blank=True)
    freeDelivery = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', related_name='products')
    images = models.ManyToManyField('Image', related_name='products', blank=True)
    reviews = models.ManyToManyField('Review', related_name='products')
    specifications = models.ManyToManyField('Specification', related_name='products')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=4.6)

    class Meta:
        db_table = 'product_full'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title


class SaleItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    images = models.ManyToManyField('Image')

    def __str__(self):
        return self.title


class Specification(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.value}"


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    text = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.text


class Review(models.Model):
    author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    rate = models.PositiveSmallIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"Review by {self.author} on {self.date}"

    def __str__(self):
        return f"{self.author}'s basket"


class Images(models.Model):
    imageUrl = models.ImageField(upload_to='images/')


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Image(models.Model):
    src = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)

    def __str__(self):
        return self.src
