from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE


class TableTop(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)
    # id = models.BigIntegerField(primary_key=True,unique=True)
    code = models.CharField(max_length=100)

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

    capacity = models.PositiveSmallIntegerField(default=0, decimal_places=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    # def clean(self):
    #     if not len(self.capacity) < 10:
    #         raise ValidationError(
    #             {'capacity': "Capacity should be 10"})

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)
