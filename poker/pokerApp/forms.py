from django import forms
from .models import Player, Match


class Loginform(forms.ModelForm):
    class Meta:
        model = Player
        
        #fields inputs
        fields = ['email', 'password']
        
        # fields attrs
        widgets = {
            'email': forms.EmailInput(attrs=
                {'placeholder': 'Your mail', 
                'title':'Your Mail'},),
            
            'password': forms.PasswordInput(attrs=
                {
                'placeholder': 'password', 
                'title':'Your password', 
                'min_length':'8'
                },),
        }


class SignInform(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        
