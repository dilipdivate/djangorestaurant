from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from user.models import User


class Item(models.Model):
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE)

    vendorId = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="related_vendor_item")

    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    type = models.PositiveSmallIntegerField(default=0)
    cooking = models.BooleanField()
    sku = models.CharField(max_length=100)
    price = models.DecimalField(
        decimal_places=2, default=0)
    quantity = models.FloatField(default=0, null=True, blank=True)
    unit = models.PositiveSmallIntegerField(default=0, decimal_places=0)
    recipe = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
