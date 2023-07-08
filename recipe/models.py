from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from item.models import Item
from ingredient.models import Ingredient

class Recipe(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    # id = models.BigIntegerField(primary_key=True,unique=True)
    # itemId = models.BigIntegerField()
    itemId = models.ForeignKey(
        Item, on_delete=models.CASCADE,related_name="related_item_recipe")

    # ingredientId = models.BigIntegerField()
    ingredientId = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE)

    quantity = models.FloatField(default=0, null=True, blank=True)
    unit = models.PositiveSmallIntegerField(default=0)
    instructions = models.TextField(null=True, blank=True)
