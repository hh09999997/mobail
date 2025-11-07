# store/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """تصنيف المنتجات (مثل هواتف – سماعات – شواحن)"""
    name = models.CharField(_("اسم التصنيف"), max_length=100, unique=True)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    """العلامة التجارية (مثل Apple – Samsung – Huawei)"""
    name = models.CharField(_("اسم العلامة التجارية"), max_length=100, unique=True)
    country = models.CharField(_("بلد المنشأ"), max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("علامة تجارية")
        verbose_name_plural = _("العلامات التجارية")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """تفاصيل المنتج"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name=_("التصنيف"))
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name="products", verbose_name=_("العلامة التجارية"))
    name = models.CharField(_("اسم المنتج"), max_length=150)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    price = models.DecimalField(_("السعر"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("المخزون"), default=0)
    image = models.ImageField(_("صورة المنتج"), upload_to="products/", blank=True, null=True)
    is_featured = models.BooleanField(_("منتج مميز"), default=False)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Review(models.Model):
    """تقييم المستخدمين للمنتجات"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", verbose_name=_("المنتج"))
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="reviews", verbose_name=_("المستخدم"))  # ✅ تم التعديل
    rating = models.PositiveSmallIntegerField(_("التقييم"), choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(_("التعليق"), blank=True, null=True)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("تقييم")
        verbose_name_plural = _("التقييمات")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.product} ({self.rating})"
