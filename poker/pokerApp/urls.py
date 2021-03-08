from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', index),
    path('players/', players),
    path('player/<int:id>', player),
    path('matches/', matches)
]
