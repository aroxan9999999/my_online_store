from rest_framework import serializers
from .models import Category, Product, Banner, Review, Tag, Subcategory, SaleItem, Image


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    def get_src(self, obj):
        return obj.src.url if obj.src else None

    class Meta:
        model = Image
        fields = ['src', 'alt']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'image', 'subcategories']


class SaleItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = SaleItem
        fields = ['id', 'title', 'price', 'salePrice', 'dateFrom', 'dateTo', 'images']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Banner
        fields = ['products']
