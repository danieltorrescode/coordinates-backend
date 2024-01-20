from django.urls import include, path
from rest_framework import routers
from .views import UsersView

router = routers.DefaultRouter()
router.register(r"users", UsersView, basename="users")

urlpatterns = [path("", include(router.urls))]
