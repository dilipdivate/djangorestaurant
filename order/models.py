from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from user.models import User


class Order(models.Model):
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE)

    vendorId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="related_vendor_order")

    token = models.CharField(max_length=100)

    class Status_Choices(models.TextChoices):
        NONE = "NONE", _("None")
        PENDING = "PENDING", _("Pending")
        PROCESSING = "PROCESSING", _("Processing")
        INPROGRESS = "IN_PROCESS", _("In Process")
        COMPLETED = "COMPLETE", _("Complete")
        DELIVERED = "DELIVERED", _("Delivered")

    status = models.CharField(
        max_length=10, choices=Status_Choices.choices, default=Status_Choices.NONE)

    def is_upperclass(self):
        return self.status in {
            self.Status_Choices.PENDING,
            self.Status_Choices.PROCESSING,
            self.Status_Choices.INPROGRESS,
            self.Status_Choices.COMPLETED,
            self.Status_Choices.DELIVERED,
        }

    subTotal = models.FloatField(
        default=0, null=True, blank=True, decimal_places=2)
    itemDiscount = models.IntegerField(
        default=0, null=True, blank=True, decimal_places=2)
    tax = models.FloatField(default=0, null=True, blank=True, decimal_places=2)
    shipping = models.FloatField(
        default=0, null=True, blank=True, decimal_places=2)
    total = models.FloatField(default=0, null=True,
                              blank=True, decimal_places=2)
    promo = models.IntegerField(
        default=0, null=True, blank=True, decimal_places=2)
    discount = models.FloatField(
        default=0, null=True, blank=True, decimal_places=2)
    grandTotal = models.FloatField(
        default=0, null=True, blank=True, decimal_places=2)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobile = models.IntegerField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=50, unique=True)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    def clean(self):
        if not len(self.mobile) == 10:
            raise ValidationError(
                {'mobile': "Mobile should be 10 digits"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
