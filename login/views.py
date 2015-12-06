from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as uauth
from django.core.urlresolvers import reverse
from .forms import Login, ResetPassword
from register.models import User as u, Person, Facility
from register.views import passwordcheck

# Create your views here.

def loginscreen(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            try:
                username = u.objects.get(pk=form.cleaned_data['username'])
                person = Person.objects.get(email=username.username)
                user = authenticate(username=username, password = form.cleaned_data['password'])
                if user:
                    if user.is_active:
                        login(request, user)
                        request.session['personpk'] = person.pk
                        request.session['role'] = person.role_id
                        request.session['fac'] = person.facility_id
                        if person.role_id == 1:
                            request.session['schoolfilter'] = 'all'
                            request.session['island'] = 'all'
                            request.session['district'] = 'all'
                        if(person.facility_id > 0):
                            f = Facility.objects.get(pk = person.facility_id)
                            request.session['hasprek'] = f.has_pre_k
                            request.session['onlyprk'] = f.is_only_pre_k
                        request.session['lname'] = 'all'
                        request.session['ulname'] = 'all'
                    if person.verified:
                        username = u.objects.get(pk = person.email_id)
                        if username.password == 'password':
                            return HttpResponseRedirect(reverse('login:reset'))
                        else:
                            return render(request,'login/landingpage.html', {'p':person})
                else:
                    HttpResponseRedirect('')
            except u.DoesNotExist:
                HttpResponseRedirect('')

    else:
        form = Login()
    return render(request,'login/login.html',{'form':form,})

@login_required
def landingpage(request):
    p = Person.objects.get(pk = request.session['personpk'])
    return render(request,'login/landingpage.html', {'p':p,})

def resetpassword(request):
    form = ResetPassword()
    if request.method == 'POST':
        form = ResetPassword(request.POST)
        if form.is_valid():
            pw1 = form.cleaned_data['new_password1']
            pw2 = form.cleaned_data['new_password2']
            oldpw = form.cleaned_data['old_password']
            pwcheck = passwordcheck(pw1)
            user = u.objects.get(pk = form.cleaned_data['username'])
            if user.password == oldpw:
                if pw1 == pw2 and pwcheck != 1:
                    user.password = form.cleaned_data['new_password2']
                    user.save()
                    auth_user = uauth.objects.get(username = form.cleaned_data['username'])
                    auth_user.set_password(pw1)
                    auth_user.save()
                    return render(request, 'login/login.html',{'form':Login(),})
    return render(request, 'login/reset.html', {'form':form,})

def logout_view(request):
    logout(request)
    return render(request,'login/login.html',{'form':Login()})
