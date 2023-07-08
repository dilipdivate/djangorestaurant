from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from item.models import Item
from order.models import Order


class OrderItem(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    # id = models.BigIntegerField(primary_key=True,unique=True)
    # orderId = models.BigIntegerField()
    orderId = models.ForeignKey(
        Order, on_delete=models.CASCADE)

    # itemId = models.BigIntegerField()
    itemId = models.ForeignKey(
        Item, on_delete=models.CASCADE)

    sku = models.CharField(max_length=100)
    price = models.FloatField(default=0, null=True,
                              blank=True, decimal_places=2)
    discount = models.FloatField(
        default=0, null=True, blank=True, decimal_places=2)
    quantity = models.FloatField(default=0, null=True, blank=True)
    unit = models.PositiveSmallIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
