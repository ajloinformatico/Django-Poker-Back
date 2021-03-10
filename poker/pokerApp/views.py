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
                return redirect('/crud/'+str(field.get_id()))
        # not player found
        ctx['error'] = 'si'
    return render(request, 'index.html', ctx)


def sigin(request):
    # if request is get ever load signinform
    if request.method == 'GET':
        ctx = {
            'sign_inform':SignInform()
        }
        return render(request, 'signin.html', ctx)
    if request.method == 'POST':
        # save data form to save
        form = SignInform(request.POST)
        ctx = {
            'sign_inform': form
        }
        form_post_values = [request.POST['name'], request.POST['surname'],
            request.POST['password'], request.POST['nick'],request.POST['email'], 
            request.POST['age'], request.POST['country'], request.POST['money']]

        # check if player exists by 3mail and name + surname
        for field in Player.objects.all():
            if field.get_email() == form_post_values[4] or field.get_name() == form_post_values[0] \
                and field.get_surname() == form_post_values[1]:
                print(form_post_values)
                ctx['error'] = 'si'
                return render(request, 'signin.html/', ctx)
        # if not find player return crud
        if form.is_valid():
            form.save()
            return redirect('/crud/'+str(field.get_id()));

def crud(request, id):
    current_player = Player.objects.get(id=id)
    matches = Match.objects.all()
    
    ctx = {
        'current_player' : current_player,
        'matches' : matches
    }
    return render(request, 'crud.html', ctx)


def add_match(request, player_id):
    ctx = dict()
    ctx['match_form'] = MatchForm()

    if request.method == 'GET':
        ctx['current_player'] = Player.objects.get(id=player_id)
    if request.method == 'POST':
        match_form = MatchForm(request.POST)
        ctx['current_player'] = Player.objects.get(id=request.POST['player_id'])
            
        if match_form.is_valid():
            match_form.save()
            ctx['match_form'] = None
            ctx['matches'] = Match.objects.all()
            return render(request, 'crud.html', ctx)

    return render(request, 'add_match.html', ctx)

def edit_match(request, player_id, team_id):
    ctx = dict()
    match = Match.objects.get(id=team_id)
    if request.method == 'GET':
        match_form = MatchForm(instance=match)
        ctx = {
            'current_player' : Player.objects.get(id= player_id),
            'match_form' : match_form
        }     
    if request.method == 'POST':
        match_form = MatchForm(request.POST, instance=match)
        ctx = {
            'current_player' : Player.objects.get(id=request.POST['player_id']),
            'match_form': match_form
        }
        if match_form.is_valid():
            match_form.save()
            ctx['matches_form'] = None
            ctx['matches'] = Match.objects.all()
            # jsut render crud content because i have ok the context
            return render(request, 'crud.html', ctx)
    

    return render(request, 'edit_match.html', ctx)

def delete_match(request, player_id, team_id):
    current_match = Match.objects.get(id=team_id)
    current_match.delete()
    ctx = {
        'current_player' : Player.objects.get(id=player_id),
        'matches' : Match.objects.all()
    }
    # redirect to crud with player id
    return render (request, 'crud.html', ctx);