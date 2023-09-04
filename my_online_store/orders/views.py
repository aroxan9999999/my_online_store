import json
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Basket, OrderItem
from .serializers import PaymentSerializer, BasketSerializer, OrderItemSerializer, \
    ProductShortSerializer, BasketSerializer, OrderSerializer
from products.models import Product
from products.serializers import ProductSerializer


class OrderView(APIView):
    def get(self, request):
        user = request.user
        active_order = Order.objects.filter(user=user, status='active').first()
        if active_order:
            serializer = OrderSerializer(active_order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No active order found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user
        order = Order.objects.create(user=user)
        order_items_data = request.data
        order_items = []
        for item_data in order_items_data:
            product_id = item_data.get('id')
            count = item_data.get('count', 1)
            try:
                product = Product.objects.get(id=product_id)
                order_item = OrderItem.objects.create(product=product, orders=order, count=count)
                order_items.append(order_item)
            except Product.DoesNotExist:
                return Response(f'Product with ID {product_id} does not exist.', status=status.HTTP_400_BAD_REQUEST)
        if order_items:
            order.products.set(order_items)
            return Response({'orderId': order.id}, status=status.HTTP_201_CREATED)

        return Response('No valid order items provided.', status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        data = request.data
        order.phone = data['phone']
        order.email = data['email']
        order.city = data['city']
        order.address = data['address']
        order.status = 'active'
        order.payment_type = data['paymentType']
        order.full_name = data['fullName']
        order.delivery_type = data.get('deliveryType')
        order.save()
        return Response(status=status.HTTP_200_OK)


class BasketView(APIView):

    def get(self, request):
        user = request.user
        basket, created = Basket.objects.get_or_create(user=user)
        total_price = sum(order_item.total_price for order_item in basket.products.all())
        basket_data = [p.product for p in basket.products.all()]
        serializer_data = ProductSerializer(basket_data, many=True)

        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        basket, created = Basket.objects.get_or_create(user=user)
        request_data = request.data
        product_id = request_data.get('id')
        quantity = request_data.get('count', 1)
        product = Product.objects.get(id=product_id)
        basket_item = OrderItem.objects.create(product=product, count=quantity)
        basket.products.add(basket_item)
        basket.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        basket = Basket.objects.get(user=user)

        product_id = request.data.get('id')
        quantity = request.data.get('count', 1)
        basket_item = basket.products.get(product__pk=product_id)
        if basket_item.count <= quantity:
            basket_item.delete()
        else:
            basket_item.count -= quantity
            basket_item.save()
            basket.save()

        serializer = ProductSerializer(basket_item.product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentView(APIView):
    def post(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
