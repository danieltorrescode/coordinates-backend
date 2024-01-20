from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Details(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(null=True, decimal_places=8, max_digits=15)
    longitude = models.DecimalField(null=True, decimal_places=8, max_digits=15)
    distance = models.DecimalField(null=True, blank=True, decimal_places=3, max_digits=7)
