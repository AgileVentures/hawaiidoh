from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateFacility, CreateUser, Username, ModifyUser, FacilityFilter
from .models import  Facility, District, Role, User, Person, Enrollment, Island
from django.contrib.auth.models import User as uauth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from reportviewing.views import StudentFilter
import operator

# Create your views here.

@login_required
def facility(request):
    if request.method =='POST':
        form = CreateFacility(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            street = form.cleaned_data['street']
            zip = form.cleaned_data['zip']
            city = form.cleaned_data['city']
            has_pre_k = form.cleaned_data['has_pre_k']
            is_only_pre_k = form.cleaned_data['is_only_pre_k']
            phone = form.cleaned_data['phone']
            fax = form.cleaned_data['fax']
            email = form.cleaned_data['email']
            district = District.objects.get(name = form.cleaned_data['district'])
            lowest_g = Enrollment.objects.get(name = form.cleaned_data['lowest_grade'])
            highest_g = Enrollment.objects.get(name = form.cleaned_data['highest_grade'])
            f = Facility(name=name,street=street,zip=zip,city=city,has_pre_k=has_pre_k,is_only_pre_k=is_only_pre_k, phone=phone, fax=fax,email=email)
            f.lowest_grade_id = lowest_g.pk
            f.highest_grade_id = highest_g.pk
            f.district_id = district.pk
            f.count = 0
            f.save()
            return HttpResponseRedirect(reverse('login:landingpage'))
    else:
        form = CreateFacility()
    return render(request,'register/facilityinput.html',{'form':form,})

@login_required
def facilitylist(request):
    form = FacilityFilter()
    if request.session['schoolfilter'] == 'all':
        object_list = Facility.objects.exclude(pk=1).order_by('name')
    else:
        object_list = Facility.objects.filter(name__icontains=request.session['schoolfilter']).order_by('name')
    if request.session['district'] != 'all':
        d = District.objects.get(pk = request.session['district'])
        object_list = object_list.filter(district_id = d.pk)
    if request.session['island'] != 'all':
        i = Island.objects.get(pk = request.session['island'] )
        districts = District.objects.filter(island_id=i.pk)
        object_list = object_list.filter(reduce(operator.or_,[Q(district_id = d.pk) for d in districts]))

    if request.method=='POST':
        form = FacilityFilter(request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] is None:
                request.session['schoolfilter'] = 'all'
            else:
                request.session['schoolfilter'] = form.cleaned_data['name']
            if form.cleaned_data['island'] is None:
                request.session['island'] = 'all'
            else:
                request.session['island'] = Island.objects.get(pk =
form.cleaned_data['island']).pk
            if form.cleaned_data['district'] is None:
                request.session['district'] = 'all'
            else:
                request.session['district'] = District.objects.get(name= form.cleaned_data['district']).pk
            return HttpResponseRedirect(reverse('register:facilitylist'))
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        fac = paginator.page(page)
    except PageNotAnInteger:
        fac = paginator.page(1)
    except EmptyPage:
        fac = paginator.page(paginator.num_pages)

    return render(request,'register/facility_list.html',{'form':form, 'object_list':fac})



def username(request):
    if request.method == 'POST':
        form = Username(request.POST)
        if form.is_valid():
            users = User.objects.filter(pk=form.cleaned_data['user'])
            if not users:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 == password2 and passwordcheck(password1) != 1:
                    u = User(username=form.cleaned_data['user'], password=password2)
                    u.save()
                    request.session['user'] = u.pk
                    return HttpResponseRedirect(reverse('register:createuser'))
    else:
        form = Username()
    return render(request, 'register/user.html',{'form':form,})


def createuser(request):
    u = request.session['user']
    request.session['user'] = u
    if request.method =='POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            fac = Facility.objects.get(name = form.cleaned_data['facility'])
            role = Role.objects.get(name = form.cleaned_data['role'])
            fname = form.cleaned_data['fname']
            mname = form.cleaned_data['mname']
            lname = form.cleaned_data['lname']
            phone = form.cleaned_data['phone']
            fax = form.cleaned_data['fax']
            title = form.cleaned_data['title']
            p = Person(fname=fname, mname=mname, lname=lname, phone=phone,fax=fax,title=title)
            p.email_id = User.objects.get(pk = u)
            p.facility_id=fac.pk
            p.role_id=role.pk
            p.save()
            uname = User.objects.get(pk = p.email_id)
            user = uauth.objects.create_user(username = uname.pk, password=uname.password, first_name = p.fname, last_name = p.lname)
            user.save()
            return HttpResponseRedirect(reverse('login:login'))
    else:
        form = CreateUser()
    return render(request, 'register/createuser.html', {'form':form,})

@login_required
def facilitylanding(request, facility_id):

    f = Facility.objects.get(pk=facility_id)
    d = District.objects.get(pk=f.district_id)
    try:
        p = Person.objects.filter(facility_id=f.pk).get(role_id=2)
    except Person.DoesNotExist:
        p = None

    if request.method == 'POST':
        request.session['inputid'] = f.pk

        if '12a' in request.POST:
                return HttpResponseRedirect(reverse('reportinput:landing12a'))
        if '12b' in request.POST:
                return HttpResponseRedirect(reverse('reportinput:landing12b'))

        if 'Med' in request.POST:
            request.session['type']=1

        if 'Rel' in request.POST:
            request.session['type']=2

        if 'Ex' in request.POST:
            request.session['type']=3

        if 'All' in request.POST:
            request.session['type']=4

        return HttpResponseRedirect(reverse('reportviewing:students'))
    else:
        return render(request, 'register/facilitylanding.html',{'f':f,'d':d,'p':p})

@login_required
def modifyfacility(request, facility_id):
    facility = Facility.objects.get(pk = facility_id)
    district = District.objects.get(pk = facility.district_id)
    if request.method == 'POST':
        form = CreateFacility(request.POST)
        if 'Delete' in request.POST:
            f = Facility.objects.get(pk = facility_id)
            f.delete()
            return HttpResponseRedirect(reverse('login:landingpage'))
        if 'Change' in request.POST:
            if form.is_valid():
                f = Facility.objects.get(pk= facility_id)
                f.name = form.cleaned_data['name']
                f.save()
                f.street = form.cleaned_data['street']
                f.save()
                f.zip = form.cleaned_data['zip']
                f.save()
                f.city = form.cleaned_data['city']
                f.save()
                f.has_pre_k = form.cleaned_data['has_pre_k']
                f.save()
                f.is_only_pre_k = form.cleaned_data['is_only_pre_k']
                f.save()
                f.phone = form.cleaned_data['phone']
                f.save()
                f.fax = form.cleaned_data['fax']
                f.save()
                f.email = form.cleaned_data['email']
                f.save()
                f.district = District.objects.get(name = form.cleaned_data['district'])
                f.save()
                f.lowest_grade = Enrollment.objects.get(name = form.cleaned_data['lowest_grade'])
                f.save()
                f.highest_grade = Enrollment.objects.get(name = form.cleaned_data['highest_grade'])
                f.save()

            return HttpResponseRedirect(reverse('login:landingpage'))

    else:
        form = CreateFacility(initial={'name':facility.name,'street':facility.street,'zip':facility.zip, 'city':facility.city, 'has_pre_k':facility.has_pre_k,'is_only_pre_k':facility.is_only_pre_k,'phone':facility.phone, 'fax':facility.fax, 'email':facility.email, 'island':district.island, 'district':facility.district, 'lowest_grade':facility.lowest_grade, 'highest_grade':facility.highest_grade})
    return render(request, 'register/modifyfac.html', {'form':form,})

@login_required
def modifyuser(request, person_id):
    person = Person.objects.get(pk = person_id)
    user = User.objects.get(pk = person.email_id)
    if request.method == 'POST':
        if 'Delete' in request.POST:
            p = Person.objects.get(pk = person_id)
            u = User.objects.get(pk = p.email_id)
            ua = uauth.objects.get(username= u.username)
            p.delete()
            u.delete()
            ua.delete()
            return HttpResponseRedirect(reverse('login:landingpage'))
        if 'Change' in request.POST:
            form = ModifyUser(request.POST)
            if form.is_valid():
                p = Person.objects.get(pk = person_id)
                u = User.objects.get(pk = person.email_id)
                u.password = form.cleaned_data['password']
                u.save()
                p.fname = form.cleaned_data['fname']
                p.save()
                p.mname = form.cleaned_data['mname']
                p.save()
                p.lname = form.cleaned_data['lname']
                p.save()
                p.phone = form.cleaned_data['phone']
                p.save()
                p.fax = form.cleaned_data['fax']
                p.save()
                p.title = form.cleaned_data['title']
                p.save()
                if request.session['role'] == 1:
                    p.role_id = form.cleaned_data['role']
                    p.save()
                    p.verified = form.cleaned_data['verify']
                    p.save()
                    p.facility_id = form.cleaned_data['facility']
                    p.save()
                user = uauth.objects.get(username = p.email_id)
                user.set_password(u.password)
                user.save()
                return HttpResponseRedirect(reverse('login:landingpage'))
        if 'Drop' in request.POST:
            p = Person.objects.get(pk = person_id)
            p.facility_id = None
            p.save()
            p.verified = False
            p.save()
            return HttpResponseRedirect(reverse('login:landingpage'))
    else:
        form = ModifyUser(initial={'fname':person.fname, 'mname':person.mname, 'lname':person.lname, 'phone':person.phone, 'fax':person.fax, 'title':person.title, 'user':user.username,'password':user.password, 'facility':person.facility, 'role':person.role, 'verify':person.verified})
    return render(request, 'register/modify_user.html', {'form':form,})

@login_required
def userfilter(request):
    form = StudentFilter()
    person = Person.objects.get(pk = request.session['personpk'])
    if person.role_id == 1:
        object_list = Person.objects.all().order_by('facility').order_by('verified')
    else:
        object_list = Person.objects.filter(facility_id=person.facility_id)

    if request.session['ulname'] != 'all':
        if person.role_id == 1:
            object_list = Person.objects.filter(lname__icontains=request.session['ulname'])
        else:
            object_list = Person.objects.filter(facility_id = person.facility_id).filter(lname__icontains=request.session['ulname'])

    if request.method=='POST':
        form = StudentFilter(request.POST)
        if form.is_valid():
            if form.cleaned_data['lname'] is None:
                request.session['ulname'] = 'all'
            else:
                request.session['ulname'] = form.cleaned_data['lname']
        return HttpResponseRedirect(reverse('register:userlist'))
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        staff = paginator.page(page)
    except PageNotAnInteger:
        staff = paginator.page(1)
    except EmptyPage:
        staff = paginator.page(paginator.num_pages)
    return render(request, 'register/person_list.html', {'object_list':staff,'form':form,})

def passwordcheck(password):
    pw = password
    caps = sum(1 for c in pw if c.isupper())
    low = sum(1 for c in pw if c.islower())
    num = sum(1 for c in pw if c.isnumeric())
    if len(pw) >= 8 and len(pw) <= 20 and caps >= 1 and low >=1 and num >= 1:
        return 0
    else:
        return 1