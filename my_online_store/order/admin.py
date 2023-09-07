from django.contrib import admin
from .models import Order, Payment


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullName', 'email', 'phone', 'status', 'createdAt']
    list_filter = ['status', 'createdAt']
    search_fields = ['fullName', 'email', 'phone']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'month', 'year']
    search_fields = ['number', 'name']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['user']
    filter_horizontal = ('products',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)

