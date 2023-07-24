from .views import *
from django.urls import path

urlpatterns = [
    path("", home.as_view(), name="")
]
