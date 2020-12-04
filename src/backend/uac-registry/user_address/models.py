# Django imports
from django.db import models

# Django extensions
from django_extensions.db.models import TimeStampedModel

# Project imports
from address.models import Address
from user.models import User


class UserAddress(TimeStampedModel):
    """A user can have many addresses, with one being the main address.
    But, two users can, for instance, live in the same address, so
    a single address can be associated with many users."""

    address = models.ForeignKey(
        Address,
        blank=True,
        related_name='addresses',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        blank=True,
        related_name='users',
        on_delete=models.CASCADE
    )
    is_main_address = models.BooleanField(default=False)
