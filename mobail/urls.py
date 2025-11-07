"""
🔗 إعداد روابط المشروع (mobail)

يقوم هذا الملف بتوزيع روابط العناوين (URLs) إلى التطبيقات المختلفة.
يشمل:
- لوحة تحكم Django
- روابط التطبيقات: store, accounts, orders
- إعداد عرض ملفات الوسائط أثناء التطوير
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ✅ لعرض ملفات media أثناء التطوير

urlpatterns = [
    # 🧭 لوحة تحكم Django الافتراضية
    path('admin/', admin.site.urls),

    # 🏠 التطبيق الرئيسي للمتجر (store)
    path('', include('store.urls')),  # الصفحة الرئيسية وعرض المنتجات

    # 👤 إدارة الحسابات والمستخدمين (accounts)
    path('accounts/', include('accounts.urls')),

    # 📦 إدارة الطلبات والسلة والمدفوعات (orders)
    path('orders/', include('orders.urls')),
]

# 🖼️ إعداد عرض ملفات الوسائط أثناء وضع التطوير (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
