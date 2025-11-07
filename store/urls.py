# store/urls.py
from django.urls import path
from django.http import HttpResponse

app_name = 'store'

def home(request):
    return HttpResponse("<h1 style='text-align:center; padding-top:50px;'>مرحباً بك في متجر الأجهزة المحمولة 🛍️</h1>")

urlpatterns = [
    path('', home, name='home'),
]
