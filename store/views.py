from django.shortcuts import render
from .models import Product

def products_view(request):
    """عرض جميع المنتجات"""
    products = Product.objects.all()  # ✅ جلب كل المنتجات من قاعدة البيانات
    return render(request, "store/products.html", {"products": products})
