from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import Request
from .models import Supportrequest
from register.models import Person
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
@login_required
def createrequest(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            sr = Supportrequest(person_id=request.session['personpk'],status_id=1,description=desc, opendate=datetime.datetime.today())
            sr.save()
            return HttpResponseRedirect(reverse('support:open'))
    else:
        form = Request()
    return render(request, 'support/createsupport.html', {'form':form,})

@login_required
def viewrequests(request):
    p = Person.objects.get(pk=request.session['personpk'])
    if p.facility_id == 1:
        tickets = Supportrequest.objects.exclude(status_id=3)
    else:
        tickets = Supportrequest.objects.filter(person_id=p.pk)
    return render(request,'support/opentickets.html',{'tickets':tickets})

@login_required
def updatesupport(request, r_id):
    sr = Supportrequest.objects.get(pk = r_id)
    sr.status_id = 2
    sr.save()
    return HttpResponseRedirect(reverse('support:open'))

@login_required
def closesupport(request, r_id):
    sr = Supportrequest.objects.get(pk = r_id)
    sr.status_id = 3
    sr.save()
    return HttpResponseRedirect(reverse('support:open'))