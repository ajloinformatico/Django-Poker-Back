from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', login, name="index"),
    path('signin/', sigin, name="signin"),
    path('crud/<int:id>', crud, name="crud"),
    path('add_match/', add_match, name="add_match"),
    path('edit_match/<int:player_id>/<int:team_id>', edit_match, name="edit_match"),
    path('delete_match/<int:player_id>/<int:team_id>', delete_match, name="delete_match")
]
