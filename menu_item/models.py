from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from menu.models import Menu
from item.models import Item

class MenuItem(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    # id = models.BigIntegerField(primary_key=True,unique=True)
    # menuId = models.BigIntegerField()
    # itemId = models.BigIntegerField()

    itemId = models.ForeignKey(
        Item, on_delete=models.CASCADE)

    menuId = models.ForeignKey(
        Menu, on_delete=models.CASCADE)

    active = models.BooleanField()

