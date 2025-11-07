# orders/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    """
    نموذج يمثل عربة التسوق المؤقتة الخاصة بالمستخدم
    """
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name=_("المستخدم"),
        help_text=_("المستخدم الذي يملك هذه السلة"),
    )
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("سلة التسوق")
        verbose_name_plural = _("سلال التسوق")
        ordering = ["-created_at"]

    def __str__(self):
        return f"سلة {self.user}"


class CartItem(models.Model):
    """
    عنصر داخل سلة التسوق
    """
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("السلة"),
        help_text=_("السلة التي يحتويها هذا العنصر"),
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        verbose_name=_("المنتج"),
        help_text=_("المنتج الذي تمت إضافته إلى السلة"),
    )
    quantity = models.PositiveIntegerField(_("الكمية"), default=1)

    class Meta:
        verbose_name = _("عنصر في السلة")
        verbose_name_plural = _("عناصر السلال")

    def __str__(self):
        return f"{self.product} × {self.quantity}"


class Order(models.Model):
    """
    نموذج الطلب النهائي بعد تأكيد الشراء
    """
    STATUS_CHOICES = [
        ("pending", "قيد المعالجة"),
        ("shipped", "تم الشحن"),
        ("delivered", "تم التسليم"),
        ("cancelled", "ملغي"),
    ]

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("المستخدم"),
        help_text=_("المستخدم الذي قام بالطلب"),
    )
    address = models.ForeignKey(
        "accounts.Address",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("عنوان الشحن"),
        help_text=_("العنوان الذي سيتم شحن الطلب إليه"),
    )
    total_price = models.DecimalField(_("الإجمالي"), max_digits=10, decimal_places=2)
    status = models.CharField(_("حالة الطلب"), max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("الطلب")
        verbose_name_plural = _("الطلبات")
        ordering = ["-created_at"]

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user}"


class OrderItem(models.Model):
    """
    نموذج يمثل عنصرًا داخل الطلب النهائي
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("الطلب"),
        help_text=_("الطلب الذي ينتمي إليه هذا العنصر"),
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("المنتج"),
        help_text=_("المنتج الذي تم طلبه"),
    )
    quantity = models.PositiveIntegerField(_("الكمية"))
    price = models.DecimalField(_("السعر الفردي"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("عنصر في الطلب")
        verbose_name_plural = _("عناصر الطلبات")

    def __str__(self):
        return f"{self.product} × {self.quantity}"


class Payment(models.Model):
    """
    تفاصيل عملية الدفع الخاصة بكل طلب
    """
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name=_("الطلب"),
        help_text=_("الطلب المرتبط بهذه العملية المالية"),
    )
    method = models.CharField(_("طريقة الدفع"), max_length=50)
    amount = models.DecimalField(_("المبلغ"), max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(_("تم الدفع بنجاح"), default=False)
    created_at = models.DateTimeField(_("تاريخ العملية"), auto_now_add=True)

    class Meta:
        verbose_name = _("عملية دفع")
        verbose_name_plural = _("عمليات الدفع")
        ordering = ["-created_at"]

    def __str__(self):
        return f"دفع {self.order.id} - {self.amount} ريال"
