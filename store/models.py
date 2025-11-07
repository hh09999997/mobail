# store/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    نموذج تصنيف المنتجات (مثل: هواتف – سماعات – شواحن)
    """
    name = models.CharField(
        _("اسم التصنيف"),
        max_length=100,
        unique=True,
        help_text=_("أدخل اسم التصنيف الرئيسي مثل: هواتف، سماعات، شواحن...")
    )
    description = models.TextField(
        _("الوصف"),
        blank=True,
        null=True,
        help_text=_("وصف اختياري يوضح محتوى هذا التصنيف")
    )
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("تصنيف المنتج")
        verbose_name_plural = _("تصنيفات المنتجات")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    نموذج العلامة التجارية (مثل Apple – Samsung – Huawei)
    """
    name = models.CharField(
        _("اسم العلامة التجارية"),
        max_length=100,
        unique=True,
        help_text=_("أدخل اسم العلامة التجارية مثل: Apple، Samsung، Huawei...")
    )
    country = models.CharField(
        _("بلد المنشأ"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("الدولة التي تنتمي إليها العلامة التجارية")
    )
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("العلامة التجارية")
        verbose_name_plural = _("العلامات التجارية")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    نموذج تفاصيل المنتجات داخل المتجر
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("التصنيف"),
        help_text=_("حدد التصنيف الذي ينتمي إليه المنتج")
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name=_("العلامة التجارية"),
        help_text=_("العلامة التجارية للمنتج (اختياري)")
    )
    name = models.CharField(_("اسم المنتج"), max_length=150)
    description = models.TextField(_("الوصف"), blank=True, null=True)
    price = models.DecimalField(
        _("السعر"),
        max_digits=10,
        decimal_places=2,
        help_text=_("أدخل السعر بالريال السعودي")
    )
    stock = models.PositiveIntegerField(
        _("المخزون"),
        default=0,
        help_text=_("عدد القطع المتوفرة من المنتج")
    )
    image = models.ImageField(
        _("صورة المنتج"),
        upload_to="products/",
        blank=True,
        null=True,
        help_text=_("قم برفع صورة المنتج")
    )
    is_featured = models.BooleanField(_("منتج مميز"), default=False)
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("المنتج")
        verbose_name_plural = _("المنتجات")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    نموذج تقييمات المستخدمين للمنتجات
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("المنتج"),
        help_text=_("المنتج الذي تم تقييمه")
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("المستخدم"),
        help_text=_("المستخدم الذي قام بكتابة التقييم")
    )
    rating = models.PositiveSmallIntegerField(
        _("التقييم"),
        choices=[(i, f"{i} نجوم") for i in range(1, 6)],
        help_text=_("أدخل تقييم المنتج من 1 إلى 5 نجوم")
    )
    comment = models.TextField(_("التعليق"), blank=True, null=True, help_text=_("تعليق المستخدم حول المنتج (اختياري)"))
    created_at = models.DateTimeField(_("تاريخ الإضافة"), auto_now_add=True)

    class Meta:
        verbose_name = _("تقييم المنتج")
        verbose_name_plural = _("تقييمات المنتجات")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.product} ({self.rating} نجوم)"
