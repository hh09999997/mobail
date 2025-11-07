from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),  # 🆕 إنشاء حساب جديد
    path('login/', views.login_view, name='login'),      # 🔐 تسجيل الدخول
    path('logout/', views.logout_view, name='logout'),   # 🚪 تسجيل الخروج
]
