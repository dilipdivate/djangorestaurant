from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from item.models import Item
from user.models import User

class ItemChef(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    # id = models.BigIntegerField(primary_key=True,unique=True)
    # itemId = models.BigIntegerField()
    # chefId = models.BigIntegerField()

    itemId = models.ForeignKey(
        Item, on_delete=models.CASCADE)
    chefId = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name="related_chef")

    active = models.BooleanField()
