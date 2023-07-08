from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
import uuid
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, User, BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, is_admin, is_staff, is_superuser, firstName, lastName, mobile, is_vendor=False, is_chef=False, is_agent=False, middleName=None, intro=False, profile=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email,username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_admin=is_admin,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            lastLogin=now,
            registeredAt=now,
            firstName=firstName,
            middleName=middleName,
            lastName=lastName,
            mobile=mobile,
            is_vendor=is_vendor,
            is_chef=is_chef,
            is_agent=is_agent,
            intro=intro,
            profile=profile,
            ** extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        # user.save()
        return user

    def create_user(self, email, username, firstName, lastName, mobile, is_vendor=False, is_chef=False, is_agent=False, middleName=None, intro=False, profile=None, password=None, **extra_fields):
        return self._create_user(email, username, False, False, False, firstName, lastName, mobile, is_vendor, is_chef, is_agent, middleName, intro, profile, password, **extra_fields)

    def create_superuser(self, email, username, firstName, lastName, mobile, is_vendor=False, is_chef=False, is_agent=False, middleName=None, intro=False, profile=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self._create_user(
            email, username, True, True, True, firstName, lastName, mobile, is_vendor, is_chef, is_agent, middleName, intro, profile, password, **extra_fields)
        return user


def validate_digit_length(mobile):
    if not (mobile.isdigit() and len(mobile) == 10):
        raise ValidationError(
            '%(mobile)s must be 10 digits', params={'mobile': mobile},)


class User(AbstractBaseUser):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    mobile = models.IntegerField(default='1234567890', validators=[
        validate_digit_length])

    email = models.EmailField(max_length=50, verbose_name="email", unique=True)
    password = models.CharField(max_length=255)
    confirmPassword = models.CharField(max_length=255)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    registeredAt = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now_add=True)
    intro = models.IntegerField(default=0, null=True, blank=True)
    profile = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstName', 'lastName', 'mobile']
    objects = MyUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff1(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_absolute_url(self):
        return "/user/%i/" % (self.pk)
