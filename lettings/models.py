from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    This model stores details about a specific address, including the street,
    city, state, zip code, and country. It also includes validation for the
    various fields to ensure proper formatting.

    Attributes:
        number (int): The street number of the address.
        street (str): The name of the street.
        city (str): The city name.
        state (str): The state or province, typically a 2-letter code.
        zip_code (int): The postal/zip code for the address.
        country_iso_code (str): The 3-character ISO country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a property available for letting.

    This model stores information about a letting property, including its title
    and the associated address. Each letting is linked to a specific address.

    Attributes:
        title (str): The title or name of the letting.
        address (Address): A one-to-one relationship with the Address model.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
