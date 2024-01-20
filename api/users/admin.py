from django.contrib import admin
from .models import Coordinates


# Register your models here.
@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    fields = ["latitude", "longitude", "distance", "user"]
