from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', login, name="index"),
    path('signin/', sigin, name="signin"),
    path('crud/<int:id>', crud, name="crud"),
    path('matches/', matches, name="matches")
]
