from django.db import models

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
# from menu_item.models import MenuItem
from user.models import User

class Menu(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    userId = models.ForeignKey(
        User, on_delete=models.CASCADE)
    # id = models.BigIntegerField(primary_key=True,unique=True)
    # userId = models.BigIntegerField()
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    type = models.IntegerField(default=0, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

