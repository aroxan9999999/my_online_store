from _decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from products.models import Product

User = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    delivery_type = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='active')
    city = models.CharField(max_length=255)
    address = models.TextField()
    products = models.ManyToManyField('OrderItem')

    def __str__(self):
        return f"Заказ №{self.id} от {self.user.username}"

    def get_total_price(self):
        total_price = self.products.aggregate(total_price=Sum('total_price'))['total_price']
        return total_price or 0


class Payment(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"Payment {self.number}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('OrderItem')


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    count = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.count * self.product.price)
        self.product.count = self.count
        self.product.price = self.total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.title} ({self.count} шт.)"
