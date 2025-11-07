# orders/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    """عربة التسوق المؤقتة"""
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="cart", verbose_name=_("المستخدم"))  # ✅ تم التعديل
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("سلة")
        verbose_name_plural = _("السلال")

    def __str__(self):
        return f"سلة {self.user}"


class CartItem(models.Model):
    """عنصر داخل السلة"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", verbose_name=_("السلة"))
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, verbose_name=_("المنتج"))
    quantity = models.PositiveIntegerField(_("الكمية"), default=1)

    class Meta:
        verbose_name = _("عنصر سلة")
        verbose_name_plural = _("عناصر السلة")

    def __str__(self):
        return f"{self.product} × {self.quantity}"


class Order(models.Model):
    """الطلب النهائي"""
    STATUS_CHOICES = [
        ("pending", "قيد المعالجة"),
        ("shipped", "تم الشحن"),
        ("delivered", "تم التسليم"),
        ("cancelled", "ملغى"),
    ]

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="orders", verbose_name=_("المستخدم"))  # ✅ تم التعديل
    address = models.ForeignKey("accounts.Address", on_delete=models.SET_NULL, null=True, verbose_name=_("العنوان"))  # ✅ تم التعديل
    total_price = models.DecimalField(_("الإجمالي"), max_digits=10, decimal_places=2)
    status = models.CharField(_("حالة الطلب"), max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)

    class Meta:
        verbose_name = _("طلب")
        verbose_name_plural = _("الطلبات")
        ordering = ["-created_at"]

    def __str__(self):
        return f"طلب {self.id} - {self.user}"


class OrderItem(models.Model):
    """عناصر الطلب"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name=_("الطلب"))
    product = models.ForeignKey("store.Product", on_delete=models.SET_NULL, null=True, verbose_name=_("المنتج"))
    quantity = models.PositiveIntegerField(_("الكمية"))
    price = models.DecimalField(_("السعر الفردي"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("عنصر طلب")
        verbose_name_plural = _("عناصر الطلبات")

    def __str__(self):
        return f"{self.product} × {self.quantity}"


class Payment(models.Model):
    """بيانات الدفع"""
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment", verbose_name=_("الطلب"))
    method = models.CharField(_("طريقة الدفع"), max_length=50)
    amount = models.DecimalField(_("المبلغ"), max_digits=10, decimal_places=2)
    is_successful = models.BooleanField(_("تم الدفع بنجاح"), default=False)
    created_at = models.DateTimeField(_("تاريخ العملية"), auto_now_add=True)

    class Meta:
        verbose_name = _("دفع")
        verbose_name_plural = _("المدفوعات")

    def __str__(self):
        return f"دفع {self.order.id} - {self.amount} ريال"
