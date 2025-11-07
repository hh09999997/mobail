from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User


def register(request):
    """🆕 إنشاء حساب جديد"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect("accounts:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل.")
            return redirect("accounts:register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.save()
        messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك تسجيل الدخول الآن.")
        return redirect("accounts:login")

    return render(request, "accounts/register.html")


def login_view(request):
    """🔐 تسجيل الدخول"""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"مرحبًا {user.username} 👋")
            return redirect("/")
        else:
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة.")

    return render(request, "accounts/login.html")
