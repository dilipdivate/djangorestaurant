from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from table_top.models import TableTop
from user.models import User


class Booking(models.Model):
    tableId = models.ForeignKey(
        TableTop, on_delete=models.CASCADE, related_name='bookings')

    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')

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
