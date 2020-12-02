# Django imports
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Client(TimeStampedModel):
    """A client data abstraction"""
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
