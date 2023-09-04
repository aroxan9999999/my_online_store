import json

from django.db.models import F

from .models import Category, Banner, Tag, SaleItem, Review
from .serializers import CategorySerializer, ProductSerializer, BannerSerializer, ReviewSerializer, SaleItemSerializer, \
    TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product


class CategoryView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CatalogView(APIView):
    def get(self, request):
        filter_params = request.query_params.get('filter', {})
        current_page = int(request.query_params.get('currentPage', 1))
        category = request.query_params.get('category')
        sort_by = request.query_params.get('sort', 'date')
        sort_type = request.query_params.get('sortType', 'dec')
        tags = request.query_params.getlist('tags')
        limit = int(request.query_params.get('limit', 20))

        filter_mapping = {
            'title__icontains': 'name',
            'price__gte': 'minPrice',
            'price__lte': 'maxPrice',
            'delivery': 'freeDelivery',
            'availability': 'available',
            'category_id': 'category',
            'tags__id__in': 'tags',
        }

        filter_args = {}
        for key, value in filter_mapping.items():
            if value in filter_params:
                filter_args[key] = filter_params[value]
        sort_key = sort_by if sort_type == 'dec' else '-' + sort_by
        products = Product.objects.filter(**filter_args).order_by(sort_key)
        total_products = products.count()
        if total_products == 0:
            last_page = 0
        else:
            last_page = (total_products - 1) // limit
        offset = (current_page - 1) * limit
        products = products[offset:offset + limit]
        serializer = ProductSerializer(products, many=True)
        json_data = serializer.data

        response_data = {
            'items': json_data,
            'currentPage': current_page,
            'lastPage': last_page
        }

        return Response(response_data, status=status.HTTP_200_OK)


class PopularProductsView(APIView):

    def get(self, request):
        popular_products = Product.objects.filter(rating__gte=4.5)
        serializer = ProductSerializer(popular_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LimitedProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SalesProductListView(APIView):
    def get(self, request):
        sales_count = SaleItem.objects.count()

        page = request.query_params.get('currentPage', 1)
        limit = 20
        offset = (int(page) - 1) * limit
        last_page = (sales_count + limit - 1) // limit

        sales = SaleItem.objects.filter().annotate(
            discounted_price=F('price') * (1 - F('salePrice') / 100)
        ).order_by('-discounted_price')[offset:offset + limit]

        serializer = SaleItemSerializer(sales, many=True)

        response_data = {
            'items': serializer.data,
            'currentPage': page,
            'lastPage': last_page
        }

        return Response(response_data, status=status.HTTP_200_OK)


class BannerViewSet(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductReviewView(APIView):

    def post(self, request, pk):
        data = json.loads(request.data)
        product = Product.objects.get(pk=pk)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            review = Review.objects.create(serializer.data)
            product.reviews.add(review)
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagListView(APIView):
    def get(self, request):
        category_id = request.query_params.get('category', None)

        if category_id is not None:
            tags = Tag.objects.filter(id=category_id)
        else:
            tags = Tag.objects.all()

        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
