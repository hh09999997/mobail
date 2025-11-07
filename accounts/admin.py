# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Address


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """لوحة تحكم المستخدمين داخل تطبيق الحسابات (accounts)"""
    list_display = ('email', 'username', 'is_customer', 'is_staff_member', 'is_superuser', 'is_active')
    list_filter = ('is_customer', 'is_staff_member', 'is_superuser', 'is_active')
    search_fields = ('email', 'username', 'phone')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('المعلومات الشخصية', {'fields': ('first_name', 'last_name', 'phone')}),
        ('الصلاحيات', {'fields': ('is_active', 'is_customer', 'is_staff_member', 'is_superuser', 'groups', 'user_permissions')}),
        ('تواريخ مهمة', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_customer', 'is_staff_member', 'is_active')}
        ),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """لوحة تحكم العناوين"""
    list_display = ('user', 'city', 'region', 'is_default', 'created_at')
    list_filter = ('is_default', 'city')
    search_fields = ('user__email', 'city', 'region')
    ordering = ('-created_at',)
