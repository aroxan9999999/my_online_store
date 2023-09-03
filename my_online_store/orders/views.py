from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Basket, OrderItem
from .serializers import OrderSerializer, PaymentSerializer, BasketSerializer, OrderItemSerializer, \
    ProductShortSerializer
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
        data = request.data
        order = Order.objects.create(
            user=request.user,
            full_name=data['full_name'],
            email=data['email'],
            phone=data['phone'],
            delivery_type=data['delivery_type'],
            payment_type=data['payment_type'],
            total_cost=data['total_cost'],
            status=data['status'],
            city=data['city'],
            address=data['address']
        )
        for basket_item in basket.products.all():
            order.products.add(basket_item.product, quantity=basket_item.count)

        # Clear the basket
        basket.products.clear()

        return Response({'orderId': order.id}, status=status.HTTP_201_CREATED)


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

        basket_data = []

        total_price = 0  # Инициализируем общую стоимость корзины

        for order_item in basket.products.all():
            product_data = {
                'id': order_item.product.id,
                'title': order_item.product.title,
                'price': order_item.product.price,
                'images': [
                    {
                        'src': image.src,
                        'alt': image.alt,
                    }
                    for image in order_item.product.images.all()
                ],
                'count': order_item.count,
                'total_price': order_item.total_price,
            }
            basket_data.append(product_data)

            total_price += order_item.total_price  # Д

        response_data = {
            'basket': basket_data,
            'basketCount': {
                'price': total_price,
            },
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        basket, created = Basket.objects.get_or_create(user=user)

        product_id = request.data.get('id')
        quantity = request.data.get('count', 1)
        print(request.data)
        product = Product.objects.get(id=product_id)
        basket_item = OrderItem.objects.create(product=product, count=quantity)
        basket.products.add(basket_item)
        basket.save()
        serializer = BasketSerializer(basket)
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

        serializer = BasketSerializer(basket)
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
