from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, Subcategory, SaleItem, Specification, Banner, Review, Tag, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['src', 'alt', 'display_image']

    def display_image(self, obj):
        if obj.src:
            return format_html('<img src="{}" width="50" height="50" />', obj.src.url)
        return 'No image'

    display_image.short_description = 'Image'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'count', 'date', 'rating', 'display_image']
    list_filter = ['category', 'tags']
    search_fields = ['title', 'description', 'fullDescription']

    def display_image(self, obj):
        image = obj.images.first()
        if image:
            return format_html('<img src="{}" width="50" height="50" />', image.src.url)
        return 'No image'

    display_image.short_description = 'Image'


class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'salePrice', 'dateFrom', 'dateTo']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['text', 'link']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'rate', 'date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1
    readonly_fields = ['display_image']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.src.url)
        return 'No image'

    display_image.short_description = 'Image'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(SaleItem, SaleItemAdmin)
admin.site.register(Specification)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
