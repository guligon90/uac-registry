# Base imports
from __future__ import unicode_literals

# Django imports
from django.utils import timezone
from django.db import models, transaction
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# Project imports
from address.models import Address
from client.models import Client


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves an User instance with the given email and password.
        """
        if not email:
            raise ValueError('The email must be informed')

        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except Exception as e:
            raise e

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """An user data abstraction"""
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # A user can have many addresses, with one being the main address.
    # But, two users can, for instance, live in the same address, so
    # a single address can be associated with many users.
    addresses = models.ManyToManyField(Address, blank=True)

    # One user belongs to a single client. Thus, a client may have
    # an association with various users.
    client = models.ForeignKey(
        Client,
        related_name='users',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
