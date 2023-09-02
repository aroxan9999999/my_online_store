from rest_framework import serializers
from .models import Order, OrderItem, Basket
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'count')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True, read_only=True)

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
    class Meta:
        model = Basket
        fields = '__all__'


class ProductShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
