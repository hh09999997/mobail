# orders/admin.py
from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Payment


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)
    ordering = ('-created_at',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('product__name', 'cart__user__email')
    ordering = ('cart',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email', 'id')
    ordering = ('-created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    ordering = ('order',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'method', 'amount', 'is_successful', 'created_at')
    list_filter = ('is_successful', 'method')
    search_fields = ('order__id',)
    ordering = ('-created_at',)
