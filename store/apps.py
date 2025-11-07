# store/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _  # ✅ لدعم الترجمة إلى العربية

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    verbose_name = _("إدارة المتجر والمنتجات")  # ✅ الاسم العربي الذي سيظهر داخل لوحة التحكم
