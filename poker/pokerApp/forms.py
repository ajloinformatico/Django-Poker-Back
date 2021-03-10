from django import forms
from .models import Player, Match


class Loginform(forms.ModelForm):
    class Meta:
        model = Player
        
        #fields inputs
        fields = ['email', 'password']
        
        # fields attrs
        widgets = {
            'email': forms.EmailInput(attrs={
                    'placeholder': 'Your mail', 
                    'title':'Your Mail'
                },),
            
            'password': forms.PasswordInput(attrs={
                    'placeholder': 'password', 
                    'title':'Your password', 
                    'min_length':'8'
                },),
        }


class SignInform(forms.ModelForm):
    class Meta:
        model = Player
        
        # fields input
        fields = ['name','surname','password','nick','email','age','country','money']
        
        # fields attrs
        widgets = {
            'name': forms.TextInput(attrs={
                    'placeholder': 'Your name',
                    'title':'Your name'
                },),

            'surname': forms.TextInput(attrs={
                    'placeholder': 'Your surname',
                    'title':'Your surname'
                },),

            'password': forms.PasswordInput(attrs={
                    'placeholder': 'password', 
                    'title':'Your password', 
                    'min_length':'8'
                },),

            'nick': forms.TextInput(attrs={
                    'placeholder': 'Your nick',
                    'title':'Your nick'
                },),

            'email': forms.EmailInput(attrs={
                    'placeholder': 'Your mail', 
                    'title':'Your Mail'
                },),
                
            'country': forms.TextInput(attrs={
                    'placeholder': 'Your country',
                    'title':'Your country'
                },),
        }


class MatchForm(forms.ModelForm):
    class Meta:
        model= Match
        fields = '__all__'

        
