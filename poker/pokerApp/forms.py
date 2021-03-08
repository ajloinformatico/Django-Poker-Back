from django import forms
from .models import Player, Match


class Loginform(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['email', 'password']



class SignInform(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
