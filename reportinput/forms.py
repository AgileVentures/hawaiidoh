from __future__ import unicode_literals
from django import forms
from .models import Student
from register.models import Enrollment, Facility
import datetime
from django.forms.extras.widgets import SelectDateWidget

day = datetime.date.today()
class StudentForm12A(forms.Form):
    fname = forms.CharField(max_length=50)
    mname = forms.CharField(max_length=50, required=False)
    lname = forms.CharField(max_length=50)
    dateofbirth = forms.DateField(widget=SelectDateWidget(years=range(day.year-20,day.year+1),empty_label=("Year","Month","Day"),),)
    age = forms.IntegerField(required=False)
    entrydate = forms.DateField(widget=SelectDateWidget(empty_label=("Year","Month","Day"),),)
    noshotrecord = forms.BooleanField(required=False)
    exempt_rel = forms.BooleanField(required=False)
    exempt_med = forms.BooleanField(required=False)
    dtap1 = forms.BooleanField(required=False)
    dtap2 = forms.BooleanField(required=False)
    dtap3 = forms.BooleanField(required=False)
    dtap4 = forms.BooleanField(required=False)
    polio1= forms.BooleanField(required=False)
    polio2 = forms.BooleanField(required=False)
    polio3 = forms.BooleanField(required=False)
    hib = forms.BooleanField(required=False)
    hepb1 = forms.BooleanField(required=False)
    hepb2 =forms.BooleanField(required=False)
    hepb3 = forms.BooleanField(required=False)
    mmr1 = forms.BooleanField(required=False)
    varicella1 = forms.BooleanField(required=False)
    pe = forms.BooleanField(required=False)
    tb = forms.BooleanField(required=False)
    notes = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Student

class StudentForm12B(forms.Form):
    fname = forms.CharField(label='First Name',max_length=50)
    mname = forms.CharField(label='Middle Name',max_length=50, required=False)
    lname = forms.CharField(label='Last Name',max_length=50)
    dateofbirth = forms.DateField(widget=SelectDateWidget(years=range(day.year-20,day.year+1),empty_label=("Year","Month","Day"),),)
    grade = forms.ModelChoiceField(Enrollment.objects.all())
    entrydate = forms.DateField(widget=SelectDateWidget(empty_label=("Year","Month","Day"),),)
    noshotrecord = forms.BooleanField(label='No Shot Record',required = False)
    exempt_rel = forms.BooleanField(label= 'Religious Exempt',required = False)
    exempt_med = forms.BooleanField(label='Medical Exempt',required = False)
    dtap1 = forms.BooleanField(required = False)
    dtap2 = forms.BooleanField(required = False)
    dtap3 = forms.BooleanField(required = False)
    dtap4 = forms.BooleanField(required = False)
    dtap5 = forms.BooleanField(required = False)
    polio1 = forms.BooleanField(required = False)
    polio2 = forms.BooleanField(required = False)
    polio3 = forms.BooleanField(required = False)
    polio4 = forms.BooleanField(required = False)
    hepb1 = forms.BooleanField(required = False)
    hepb2 = forms.BooleanField(required = False)
    hepb3 = forms.BooleanField(required = False)
    mmr1 = forms.BooleanField(required = False)
    mmr2 = forms.BooleanField(required = False)
    varicella1 = forms.BooleanField(required = False)
    varicella2 = forms.BooleanField(required = False)
    pe = forms.BooleanField(required = False)
    tb = forms.BooleanField(required = False)
    notes = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Student

class SchoolInfo(forms.Form):
    kinder_enroll = forms.IntegerField(required=False)
    lowest_grade = forms.ModelChoiceField(Enrollment.objects.exclude(pk=1))
    highest_grade = forms.ModelChoiceField(Enrollment.objects.exclude(pk=1))
    other_enroll = forms.IntegerField()
    seventh_grade_enroll = forms.IntegerField(required=False)
    students_to_input = forms.IntegerField()

    class Meta:
        model = Facility


class PreKInfo(forms.Form):
    under19 = forms.IntegerField(label= 'Children Under 19 Months')
    over19 = forms.IntegerField(label= 'Children 19 Months and Older')
    students = forms.IntegerField(label= 'Number of Students to Input')