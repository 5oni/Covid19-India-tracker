
from django.urls import path

from . import views

urlpatterns = [
    path("", views.globalD, name="tracks"),
    path("nation/", views.Track, name="track")
]
