from __future__ import unicode_literals
from django import forms
from register.models import User, Person
from django.forms import PasswordInput
class Login(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=PasswordInput(), max_length=50)

    class Meta:
        model = User

class ResetPassword(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class' : 'form-control p30'}))
    new_password1 = forms.CharField(label="New Password", max_length=50, widget=forms.PasswordInput(attrs={'class' : 'form-control p30'}))
    new_password2 = forms.CharField(label="Confirm New Password", max_length=50, widget=forms.PasswordInput(attrs={'class' : 'form-control p30'}))

    class Meta:
        model = User