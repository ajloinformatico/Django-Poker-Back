from django.shortcuts import render

# Create your views here.
'''
path('', views.index),
    path('jugadores/', views.players),
    path('jugador/<int:id>', views.player),
    path('partidas/', views.matches)
'''


def index(request):
    return "index"


def players(request):
    return "players"


def player(request, id):
    return "players"


def matches(request):
    return "matches"
