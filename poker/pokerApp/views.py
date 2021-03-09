from django.shortcuts import render, redirect
from .models import Player, Match
from .forms import *


def login(request):
    ctx = {
        'login_form': Loginform()
    }
    # Check if there is a form
    if request.method == 'POST':
        form_post_values = [request.POST['email'], request.POST['password']]
        # loop the query separating by lists
        for field in Player.objects.all():
            if field.get_email() == form_post_values[0] and \
                    field.get_password() == form_post_values[1]:
                # Find player
                ctx = [request.POST['email']]
                #redirect ru crud view with player id
                return redirect('crud/'+str(field.get_id()))
        # not player found
        ctx['error'] = 'si'
    return render(request, 'index.html', ctx)


def sigin(request):
    # if request is get ever load signinform
    if request.method == 'GET':
        ctx = {
            'sign_inform':SignInform()
        }
        print("hy")
        return render(request, 'signin.html', ctx)
    if request.method == 'POST':
        # save data form
        form = SignInform(request.POST)
        ctx = {
            'sign_inform': form
        }
        form_post_values = [request.POST['name'], request.POST['surname'],
            request.POST['password'], request.POST['nick'], request.POST['nick'],
            request.POST['email'], request.POST['age'], request.POST['country'],
            request.POST['money'], request.POST['matches'],request.POST['avatar']]

        # loop on all players if found player send error
        for field in Player.objects.all():
            if str(field).split(" ")[1] == form_post_values[0] or str(field).split(" ")[2] == form_post_values[1]:
                print(form_post_values)
                ctx['error'] = 'si'
                return render(request, 'signin.html/', ctx)
        # if not find player return crud
        if form.is_valid():
            form.save()
            # TODO FILTER WITH PLAYER MATCHES
            return redirect('crud/'+field.id);

def crud(request, id):
    current_player = Player.objects.get(id=id)
    ctx = {
        'current_player' : current_player
    }
    return render(request, 'crud.html', ctx)


def matches(request):
    return render(request, 'matches.html')
