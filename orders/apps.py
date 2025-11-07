# orders/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _  # ✅ لدعم الترجمة العربية

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = _("إدارة الطلبات")  # ✅ الاسم الذي سيظهر بالعربية في لوحة التحكم
