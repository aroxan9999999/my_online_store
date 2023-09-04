from django.contrib import admin
from .models import Order, Payment, Basket, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    inlines = [OrderItemInline, ]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'month', 'year']
    search_fields = ['number', 'name']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user']
    filter_horizontal = ('products',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Basket, BasketAdmin)
