import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, ProductOrder
from .serializers import PaymentSerializer, \
    ProductShortSerializer, OrderSerializer
from products.models import Product
from products.serializers import ProductSerializer


class OrderView(APIView):
    def get(self, request):
        user = request.user
        active_order = Order.objects.filter(user=user)
        if active_order:
            serializer = OrderSerializer(active_order, many=True)
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
            product = Product.objects.get(id=product_id)
            order_product = ProductOrder(
                title=product.title,
                category=product.category,
                price=product.price,
                count=count,
                date=product.date,
                description=product.description,
                fullDescription=product.fullDescription,
                freeDelivery=product.freeDelivery,
                rating=product.rating,
            )
            order_product.save()  # Сначала сохраните order_product

            for image in product.images.all():
                order_product.images.add(image)  # Затем добавьте изображения

            order_product.save()
            order_items.append(order_product)

        order.products.set(order_items)
        order.status = "accepted"
        order.save()

        return Response({'orderId': order.id}, status=status.HTTP_201_CREATED)


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
        order.paymentType = data.get("paymentType", 'no payment type')
        order.fullName = data['fullName']
        order.deliveryType = data.get('deliveryType', 'free')
        order.save()
        return Response(status=status.HTTP_200_OK)


class BasketView(APIView):
    def get(self, request):
        session = request.session
        basket = session.get('basket', {})
        total_price = sum(float(item['price']) for item in basket.values())
        basket_data = [self.get_product_data(product_id) for product_id in basket.keys()]
        return Response(basket_data, status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('id')
        quantity = int(request.data.get('count', 1))
        product = self.get_product_data(product_id)
        session = request.session
        basket = session.get('basket', {})
        basket_item = basket.get(str(product_id), None)
        if basket_item:
            basket_item['count'] += quantity

        else:
            product['count'] = 1
            product['count'] += quantity
            basket[str(product_id)] = product
        session['basket'] = basket
        session.save()
        return Response([self.get_product_data(key) for key in basket.keys()], status=200)

    def delete(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            product_id = data.get('id')
            quantity = int(data.get('count', 1))
            session = request.session
            basket = session.get('basket', {})
            print(product_id)
            basket_item = basket.get(str(product_id), None)
            print(basket)
            if basket_item['count'] <= quantity:
                del basket[str(product_id)]
            else:
                basket_item['count'] -= quantity

            session['basket'] = basket
            session.save()
            serializers = [self.get_product_data(key) for key in basket.keys()]
            return Response(serializers, status=200)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=400)

    def get_product_data(self, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            product_data = ProductSerializer(product)
            return product_data.data
        except Product.DoesNotExist:
            return None


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
