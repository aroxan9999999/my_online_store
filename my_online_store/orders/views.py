import json
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
        basket = Basket.objects.filter(user=user).first()
        if not basket:
            return Response({'message': 'Basket is empty'}, status=status.HTTP_400_BAD_REQUEST)

        print(request.data)

        basket.products.clear()
        serializer = OrderSerializer(order)
        return Response({'orderId': order.id, 'order': serializer.data}, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    def get(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the order based on the request data
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        print(request.data)
        product = Product.objects.get(id=product_id)
        basket_item = OrderItem.objects.create(product=product, count=quantity)
        basket.products.add(basket_item)
        basket.save()
        serializer = ProductSerializer(product)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        basket, created = Basket.objects.get_or_create(user=user)

        product_id = request.data.get('id')
        quantity = request.data.get('count', 1)
        basket_item = basket.products.get(product=product_id)
        if basket_item.count <= quantity:
            basket_item.delete()
        else:
            basket_item.count -= quantity
            basket_item.save()
            basket.save()

        serializer = ProductSerializer(basket_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentView(APIView):
    def post(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            pass
            return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
