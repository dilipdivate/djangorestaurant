from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from order.models import Order
from user.models import User

class Transaction(models.Model):

    userId = models.ForeignKey(
        User, on_delete=models.CASCADE)

    vendorId = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name="related_vendor_transaction")

    orderId = models.ForeignKey(
        Order, on_delete=models.CASCADE)

    code = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField(default=0)
    mode = models.PositiveSmallIntegerField(default=0)
    class Status_Choices(models.TextChoices):
        NONE = "NONE", _("None")
        PENDING = "PENDING", _("Pending")
        PROCESSING = "PROCESSING", _("Processing")
        INPROGRESS = "IN_PROCESS", _("In Process")
        COMPLETED = "COMPLETE", _("Complete")
        DELIVERED = "DELIVERED", _("Delivered")

    status = models.CharField(max_length=10,choices=Status_Choices.choices,default=Status_Choices.NONE)
    def is_upperclass(self):
        return self.status in {
            self.Status_Choices.PENDING,
            self.Status_Choices.PROCESSING,
            self.Status_Choices.INPROGRESS,
            self.Status_Choices.COMPLETED,
            self.Status_Choices.DELIVERED,
        }

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)


    # def clean(self):
    #     if not len(self.mobile) == 10:
    #         raise ValidationError(
    #             {'mobile': "Mobile should be 10 digits"})

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)