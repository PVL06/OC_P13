from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User profile model extending Django's built-in User model.

    Each profile is linked to one user and stores additional information,
    such as the user's favorite city.

    Attributes:
        user (User): The user associated with this profile.
        favorite_city (str): An optional field to store the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
