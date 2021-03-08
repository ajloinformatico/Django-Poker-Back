from django.shortcuts import render, redirect
from .models import Player, Match
from .forms import Loginform, SignInform


def login(request):
    ctx = {
        'login_form': Loginform()
    }
    # Check if there is a form
    if request.method == 'POST':
        form_post_values = [request.POST['email'], request.POST['password']]
        # loop the query separating by lists
        for field in Player.objects.all():
            if str(field).split(" ")[1] == form_post_values[0] and \
                    str(field).split(" ")[2] == form_post_values[1]:
                # Find player
                ctx = [request.POST['email']]
                return render(crud, 'crud', ctx)
        # not player found
        ctx['error'] = 'si'
    return render(request, 'index.html', ctx)


def sigin(request):
    return render(request, 'signin.html')


def crud(request, id):
    return render(request, 'crud.html')


def matches(request):
    return render(request, 'matches.html')
