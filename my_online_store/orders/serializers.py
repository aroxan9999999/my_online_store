from rest_framework import serializers
from .models import Order, OrderItem, Basket
from products.serializers import ProductSerializer

from products.models import Product
from products.serializers import ImageSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer):
    orderId = serializers.IntegerField()


class PaymentSerializer(serializers.Serializer):
    payment_method = serializers.CharField(max_length=100)
    card_number = serializers.CharField(max_length=16)
    expiration_date = serializers.DateField()
    cvv = serializers.CharField(max_length=4)

    def validate_payment_method(self, value):
        return value

    def validate_card_number(self, value):
        return value

    def validate_expiration_date(self, value):
        return value

    def validate_cvv(self, value):
        return value


class BasketSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['']


class ProductShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
