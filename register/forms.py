from __future__ import unicode_literals
from django import forms
from .models import Facility, Person, Role, Island, District, User, Enrollment

class CreateFacility(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control p60'}))
    street = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control p60'}))
    zip = forms.IntegerField(max_value=99999, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    phone = forms.IntegerField(max_value=9999999999, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    fax = forms.IntegerField(max_value=9999999999, required=False, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    has_pre_k = forms.BooleanField(required=False)
    is_only_pre_k = forms.BooleanField(required=False)
    island = forms.ModelChoiceField(Island.objects.all())
    district = forms.ModelChoiceField(District.objects.all())
    lowest_grade = forms.ModelChoiceField(Enrollment.objects.all())
    highest_grade = forms.ModelChoiceField(Enrollment.objects.all())

    class Meta:
        model = Facility

class CreateUser(forms.Form):
    fname = forms.CharField(max_length=50)
    mname = forms.CharField(max_length=50, required=False)
    lname = forms.CharField(max_length=50)
    phone = forms.IntegerField(max_value=9999999999)
    fax = forms.IntegerField(max_value=9999999999, required=False)
    title = forms.CharField(max_length=50, required=False)
    facility = forms.ModelChoiceField(Facility.objects.exclude(pk = 1).order_by('name'))
    role = forms.ModelChoiceField(Role.objects.exclude(id = 1))
    class Meta:
        model = Person

class ModifyUser(forms.Form):
    fname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control p60'}))
    mname = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'form-control p60'}))
    lname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    phone = forms.IntegerField(max_value=9999999999, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    fax = forms.IntegerField(max_value=99999999999, required=False, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    title = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    user = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control p30'}))
    facility = forms.ModelChoiceField(Facility.objects.all().order_by('name'), required=False)
    role = forms.ModelChoiceField(Role.objects.all(), required=False)
    verify = forms.BooleanField(required=False)

class Username(forms.Form):
    user = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control p60'}))
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class' : 'form-control p60'}))
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class' : 'form-control p60'}))
    class Meta:
        model = User

class FacilityFilter(forms.Form):
    name = forms.CharField(required=False)
    island = forms.ModelChoiceField(Island.objects.all(), required=False)
    district = forms.ModelChoiceField(District.objects.all(), required=False)