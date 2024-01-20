from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Coordinates(models.Model):
    latitude = models.DecimalField(null=False, decimal_places=5, max_digits=8)
    longitude = models.DecimalField(null=False, decimal_places=5, max_digits=8)
    distance = models.DecimalField(null=False, decimal_places=3, max_digits=7)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
