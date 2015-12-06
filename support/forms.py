from __future__ import unicode_literals
from django import forms
from .models import Supportrequest

class Request(forms.ModelForm):
    class Meta:
        model = Supportrequest
        fields = ['description']
