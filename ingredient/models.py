from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from user.models import User


class Ingredient(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    # id = models.BigIntegerField(primary_key=True,unique=True)
    # userId = models.BigIntegerField()
    # vendorId = models.BigIntegerField()
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ingredients")
    vendorId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vendor_ingredients")

    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    type = models.PositiveSmallIntegerField(default=0)
    sku = models.CharField(max_length=100)
    quantity = models.FloatField(
        default=0, null=True, blank=True)
    unit = models.PositiveSmallIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
