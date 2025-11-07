# store/admin.py
from django.contrib import admin
from .models import Category, Brand, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'created_at')
    search_fields = ('name', 'country')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'stock', 'is_featured', 'created_at')
    list_filter = ('category', 'brand', 'is_featured')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_featured')
    ordering = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('product__name', 'user__username')
    ordering = ('-created_at',)
