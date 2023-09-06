from _decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from products.models import Product
from copy import deepcopy

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    deliveryType = models.CharField(max_length=255, blank=True, null=True)
    paymentType = models.CharField(max_length=255, blank=True, null=True)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='active', blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    products = models.ManyToManyField('ProductOrder')

    def __str__(self):
        return f"Заказ №{self.id} от {self.fullName}"

    def get_total_price(self):
        total_price = sum([p.get_total() for p in self.products.all()])
        return total_price or 0

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.totalCost = Decimal(self.get_total_price())
        return self.totalCost


class Payment(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"Payment {self.number}"


class ProductOrder(Product):
    pass