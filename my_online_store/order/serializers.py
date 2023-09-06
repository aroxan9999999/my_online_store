from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer
from products.models import Product
from products.serializers import ImageSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'createdAt',
            'fullName',
            'email',
            'phone',
            'deliveryType',
            'paymentType',
            'totalCost',
            'status',
            'city',
            'address',
            'products',
        )


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


class ProductShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
