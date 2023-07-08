from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from django.contrib.auth.models import User
# from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.authtoken.models import Token


# post_save.connect(createProfile, sender=User)
# # post_save.connect(updateUser, sender=Profile)
# # post_delete.connect(deleteUser, sender=Profile)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
