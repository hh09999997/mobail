# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    نموذج المستخدم المخصص داخل تطبيق الحسابات (accounts)
    يدعم البريد الإلكتروني كوسيلة تسجيل دخول رئيسية
    """
    email = models.EmailField(_("البريد الإلكتروني"), unique=True)
    phone = models.CharField(_("رقم الجوال"), max_length=20, blank=True, null=True)
    is_customer = models.BooleanField(_("عميل"), default=True)
    is_staff_member = models.BooleanField(_("عضو فريق المتجر"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("المستخدم")
        verbose_name_plural = _("المستخدمون")
        ordering = ["id"]
        permissions = [
            ("can_view_customers", "يمكنه عرض العملاء"),
            ("can_manage_staff", "يمكنه إدارة طاقم المتجر"),
        ]

    def __str__(self):
        return self.get_full_name() or self.email or self.username


class Address(models.Model):
    """
    نموذج عناوين المستخدمين
    يحتوي على بيانات الشحن والفواتير الخاصة بالمستخدمين
    """
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("المستخدم"),
        help_text=_("المستخدم المرتبط بهذا العنوان"),
    )
    full_name = models.CharField(_("الاسم الكامل"), max_length=150)
    city = models.CharField(_("المدينة"), max_length=100)
    region = models.CharField(_("المنطقة / الحي"), max_length=100, blank=True, null=True)
    street = models.CharField(_("الشارع / رقم المنزل"), max_length=255)
    postal_code = models.CharField(_("الرمز البريدي"), max_length=20, blank=True, null=True)
    phone = models.CharField(_("رقم التواصل"), max_length=20)
    is_default = models.BooleanField(_("العنوان الافتراضي"), default=False)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("العنوان")
        verbose_name_plural = _("العناوين")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.city}"
