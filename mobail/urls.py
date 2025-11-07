"""
URL configuration for mobail project.

The `urlpatterns` list routes URLs to views.
For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # ✅ تم إضافة include

urlpatterns = [
    # 🧭 لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 🏠 التطبيق الرئيسي للمتجر (store)
    path('', include('store.urls')),  # الصفحة الرئيسية وعرض المنتجات

    # 👤 إدارة الحسابات والمستخدمين (accounts)
    path('accounts/', include('accounts.urls')),

    # 📦 إدارة الطلبات والسلة (orders)
    path('orders/', include('orders.urls')),
]
