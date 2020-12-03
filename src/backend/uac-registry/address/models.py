# Django imports
from django.db import models
from django.core.validators import RegexValidator

# Django extensions imports
from django_extensions.db.models import TimeStampedModel

# Project imports
from address.components import format_address, PublicPlaces, States


# Information about the postal code format:
# https://rogertakemiya.com.br/gerador-de-cep-codigo-postal/"""
postal_code_validator = RegexValidator(
    regex=r'^[0-9]{8}$',
    message='The postal code must be in the format 01234567'
)


class Address(TimeStampedModel):
    city = models.CharField(max_length=100)

    # Bairro
    district = models.CharField(max_length=100, blank=True)

    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    # Complemento
    additional_info = models.CharField(max_length=100, blank=True)

    # CEP (código de endereçaento postal)
    postal_code = models.CharField(
        max_length=8,
        validators=[postal_code_validator]
    )

    # Abbrevations for public places don't have a unique size
    public_place = models.CharField(
        max_length=PublicPlaces.max_len(),
        choices=PublicPlaces.choices()
    )

    # RS, SC, ...
    state = models.CharField(
        max_length=2,
        choices=States.choices()
    )

    is_main_address = models.BooleanField(default=False)

    def __str__(self):
        return format_address(**self.__dict__)
