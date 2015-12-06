from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import Student, Report
from register.models import Person, Facility, Enrollment
from .forms import StudentForm12A, StudentForm12B, SchoolInfo, PreKInfo
import datetime
# Create your views here.

#calculate age
def calc_age(born):
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if age > 0:
        return age
    else:
        return 1

@login_required
def epi12a(request):
    formset = formset_factory(StudentForm12A, extra=request.session['students'])
    if request.method =='POST':
        formset = formset(request.POST, request.FILES)
        r = getreport(request, 'create')
        f = getfacility(request, r)
        for form in formset:
            if form.is_valid():
                id = f.district_id * 10000000000
                id += (f.pk*1000000)
                id += f.count
                f.count += 1
                f.save()
                s = Student(id = id)
                s.fname = form.cleaned_data['fname']
                s.mname = form.cleaned_data['mname']
                s.lname = form.cleaned_data['lname']
                s.dateofbirth = form.cleaned_data['dateofbirth']
                s.age = calc_age(form.cleaned_data['dateofbirth'])
                s.entry_date = form.cleaned_data['entrydate']
                s.noshotrecord = form.cleaned_data['noshotrecord']
                s.exempt_rel = form.cleaned_data['exempt_rel']
                s.exempt_med = form.cleaned_data['exempt_med']
                s.dtap1 = form.cleaned_data['dtap1']
                s.dtap2 = form.cleaned_data['dtap2']
                s.dtap3 = form.cleaned_data['dtap3']
                s.dtap4 = form.cleaned_data['dtap4']
                s.polio1 = form.cleaned_data['polio1']
                s.polio2 = form.cleaned_data['polio2']
                s.polio3 = form.cleaned_data['polio3']
                s.hib = form.cleaned_data['hib']
                s.hepb1 = form.cleaned_data['hepb1']
                s.hepb2 = form.cleaned_data['hepb2']
                s.hepb3 = form.cleaned_data['hepb3']
                s.mmr1 = form.cleaned_data['mmr1']
                s.varicella1 = form.cleaned_data['varicella1']
                s.pe = form.cleaned_data['pe']
                s.tb = form.cleaned_data['tb']
                s.notes = form.cleaned_data['notes']
                s.facility_id = f.pk
                if s.dtap1:
                    s.dtap2 = s.dtap1
                if s.dtap2:
                    s.dtap3 = s.dtap2
                if s.dtap3:
                    s.dtap4 = s.dtap3
                if s.polio1:
                    s.polio2 = s.polio1
                if s.polio2:
                    s.polio3 = s.polio2
                if s.hepb1:
                    s.hepb2 = s.hepb1
                if s.hepb2:
                    s.hepb3 = s.hepb2
                s.save()
                s.report.add(r)
        return HttpResponseRedirect(reverse('reportinput:complete'))
    else:
        formset = formset()
    return render(request, 'reportinput/epi12a.html',{'formset':formset,})

@login_required
def epi12b(request):
    formset = formset_factory(StudentForm12B, extra=request.session['students'])
    if request.method =='POST':
        r = getreport(request, 'create')
        f = getfacility(request, r)
        formset = formset(request.POST, request.FILES)
        for form in formset:
            if form.is_valid():
                grade = Enrollment.objects.get(name= form.cleaned_data['grade'])
                id = f.district_id * 10000000000
                id += (f.pk*1000000)
                id += f.count
                f.count += 1
                f.save()
                s = Student(id = id)
                s.fname = form.cleaned_data['fname']
                s.mname = form.cleaned_data['mname']
                s.lname = form.cleaned_data['lname']
                s.dateofbirth = form.cleaned_data['dateofbirth']
                s.enrollment_id = grade.pk
                s.entry_date = form.cleaned_data['entrydate']
                s.noshotrecord = form.cleaned_data['noshotrecord']
                s.exempt_rel = form.cleaned_data['exempt_rel']
                s.exempt_med = form.cleaned_data['exempt_med']
                s.dtap1 = form.cleaned_data['dtap1']
                s.dtap2 = form.cleaned_data['dtap2']
                s.dtap3 = form.cleaned_data['dtap3']
                s.dtap4 = form.cleaned_data['dtap4']
                s.dtap5 = form.cleaned_data['dtap5']
                s.polio1 = form.cleaned_data['polio1']
                s.polio2 = form.cleaned_data['polio2']
                s.polio3 = form.cleaned_data['polio3']
                s.polio4 = form.cleaned_data['polio4']
                s.hepb1 = form.cleaned_data['hepb1']
                s.hepb2 = form.cleaned_data['hepb2']
                s.hepb3 = form.cleaned_data['hepb3']
                s.mmr1 = form.cleaned_data['mmr1']
                s.mmr2 = form.cleaned_data['mmr2']
                s.varicella1 = form.cleaned_data['varicella1']
                s.varicella2 =form.cleaned_data['varicella2']
                s.pe = form.cleaned_data['pe']
                s.tb = form.cleaned_data['tb']
                s.notes = form.cleaned_data['notes']
                s.facility_id = f.pk
                if s.dtap1:
                    s.dtap2 = s.dtap1
                if s.dtap2:
                    s.dtap3 = s.dtap2
                if s.dtap3:
                    s.dtap4 = s.dtap3
                if s.dtap4:
                    s.dtap5 = s.dtap4
                if s.polio1:
                    s.polio2 = s.polio1
                if s.polio2:
                    s.polio3 = s.polio2
                if s.polio3:
                    s.polio4 = s.polio3
                if s.hepb1:
                    s.hepb2 = s.hepb1
                if s.hepb2:
                    s.hepb3 = s.hepb2
                if s.mmr1:
                    s.mmr2 = s.mmr1
                if s.varicella1:
                    s.varicella2 = s.varicella1
                s.save()
                s.report.add(r)
        return HttpResponseRedirect(reverse('reportinput:complete'))

    else:
        formset = formset()
    return render(request, 'reportinput/epi12b.html',{'formset':formset,})

def getfacility(request, object):
    p = Person.objects.get(pk = request.session['personpk'])
    if p.role_id == 1:
        if object.facility_id is None:
            f = Facility.objects.get(pk = p.facility_id)
        else:
            f = Facility.objects.get(pk = object.facility_id)
    else:
        f = Facility.objects.get(pk = p.facility_id)
    return f

def getreport(request, type):
    p = Person.objects.get(pk = request.session['personpk'])
    if p.role_id == 1:
        f = Facility.objects.get(pk = request.session['inputid'])
    else:
        f = Facility.objects.get(pk = p.facility_id)
    if type == 'update':
        report = Report.objects.filter(facility_id = f.pk)
        return report.last()
    else:
        if not f.compliant:
            r = Report.objects.filter(facility_id=f.id).filter(complete=False)
            if r:
                r = r[0]
            else:
                r = Report(person_id=p.pk, facility_id=p.facility_id,entrydate=datetime.datetime.today())
                r.save()
        else:
            r = Report(person_id=p.pk, facility_id=p.facility_id,entrydate=datetime.datetime.today())
            r.save()
            f.compliant = False
            f.save()
            students = Student.objects.filter(facility_id = r.facility_id)
            if students:
                for student in students:
                    student.report.add(r)
        return r

@login_required
def update12b(request, student_id):
    student = Student.objects.get(pk = student_id)
    f = getfacility(request, student)
    report = getreport(request, 'update')
    f.compliant = False
    form = StudentForm12B(initial={
        'fname':student.fname,
        'mname':student.mname,
        'lname':student.lname,
        'dateofbirth':student.dateofbirth,
        'grade':student.enrollment,
        'noshotrecord':student.noshotrecord,
        'exempt_rel':student.exempt_rel,
        'exempt_med':student.exempt_med,
        'dtap1':student.dtap1,
        'dtap2':student.dtap2,
        'dtap3':student.dtap3,
        'dtap4':student.dtap4,
        'dtap5':student.dtap5,
        'polio1':student.polio1,
        'polio2':student.polio2,
        'polio3':student.polio3,
        'polio4':student.polio4,
        'hepb1':student.hepb1,
        'hepb2':student.hepb2,
        'hepb3':student.hepb3,
        'mmr1':student.mmr1,
        'mmr2':student.mmr2,
        'varicella1':student.varicella1,
        'varicella2':student.varicella2,
        'pe':student.pe,
        'tb':student.tb,
        'notes':student.notes})
    if request.method == 'POST':
        form = StudentForm12B(request.POST)
        if 'Delete' in request.POST:
            s = Student(id = student.pk)
            s.delete()
            return HttpResponseRedirect(reverse('reportinput:complete'))
        if form.is_valid():
            grade = Enrollment.objects.get(name= form.cleaned_data['grade'])
            s = Student(id = student.id)
            s.fname = form.cleaned_data['fname']
            s.mname = form.cleaned_data['mname']
            s.lname = form.cleaned_data['lname']
            s.dateofbirth = form.cleaned_data['dateofbirth']
            s.enrollment_id = grade.pk
            s.entry_date = form.cleaned_data['entrydate']
            s.noshotrecord = form.cleaned_data['noshotrecord']
            s.exempt_rel = form.cleaned_data['exempt_rel']
            s.exempt_med = form.cleaned_data['exempt_med']
            s.dtap1 = form.cleaned_data['dtap1']
            s.dtap2 = form.cleaned_data['dtap2']
            s.dtap3 = form.cleaned_data['dtap3']
            s.dtap4 = form.cleaned_data['dtap4']
            s.dtap5 = form.cleaned_data['dtap5']
            s.polio1 = form.cleaned_data['polio1']
            s.polio2 = form.cleaned_data['polio2']
            s.polio3 = form.cleaned_data['polio3']
            s.polio4 = form.cleaned_data['polio4']
            s.hepb1 = form.cleaned_data['hepb1']
            s.hepb2 = form.cleaned_data['hepb2']
            s.hepb3 = form.cleaned_data['hepb3']
            s.mmr1 = form.cleaned_data['mmr1']
            s.mmr2 = form.cleaned_data['mmr2']
            s.varicella1 = form.cleaned_data['varicella1']
            s.varicella2 = form.cleaned_data['varicella2']
            s.pe = form.cleaned_data['pe']
            s.tb = form.cleaned_data['tb']
            s.notes = form.cleaned_data['notes']
            if 'Drop' in request.POST:
                s.facility_id = None
            else:
                s.facility_id = f.pk
            s.save()
            if s.dtap1:
                s.dtap2 = s.dtap1
                s.save()
            if s.dtap2:
                s.dtap3 = s.dtap2
                s.save()
            if s.dtap3:
                s.dtap4 = s.dtap3
                s.save()
            if s.dtap4:
                s.dtap5 = s.dtap4
            if s.polio1:
                s.polio2 = s.polio1
                s.save()
            if s.polio2:
                s.polio3 = s.polio2
                s.save()
            if s.polio3:
                s.polio4 = s.polio3
                s.save()
            if s.hepb1:
                s.hepb2 = s.hepb1
                s.save()
            if s.hepb2:
                s.hepb3 = s.hepb2
                s.save()
            if s.mmr1:
                s.mmr2 = s.mmr1
                s.save()
            if s.varicella1:
                s.varicella2 = s.varicella1
                s.save()
            s.save()
            if report is not None:
                report.save()
                report.student_set.add(s)
            return HttpResponseRedirect(reverse('reportinput:complete'))
    return render(request,'reportinput/studentupdate12b.html', {'form':form,'f':f})

@login_required
def update12a(request, student_id):
    student = Student.objects.get(pk = student_id)
    f = getfacility(request, student)
    rep = getreport(request, 'update')
    form = StudentForm12A(initial={
        'fname':student.fname,
        'mname':student.mname,
        'lname':student.lname,
        'dateofbirth':student.dateofbirth,
        'age':student.age,
        'noshotrecord':student.noshotrecord,
        'exempt_rel':student.exempt_rel,
        'exempt_med':student.exempt_med,
        'dtap1':student.dtap1,
        'dtap2':student.dtap2,
        'dtap3':student.dtap3,
        'dtap4':student.dtap4,
        'polio1':student.polio1,
        'polio2':student.polio2,
        'polio3':student.polio3,
        'hib':student.hib,
        'hepb1':student.hepb1,
        'hepb2':student.hepb2,
        'hepb3':student.hepb3,
        'mmr1':student.mmr1,
        'varicella1':student.varicella1,
        'pe':student.pe,
        'tb':student.tb,
        'notes':student.notes})
    if request.method == 'POST':
        form = StudentForm12A(request.POST)
        if 'Delete' in request.POST:
            s = Student(id = student.pk)
            s.delete()
            return HttpResponseRedirect(reverse('reportinput:complete'))
        if form.is_valid():
            s = Student(id = student.id)
            s.fname = form.cleaned_data['fname']
            s.mname = form.cleaned_data['mname']
            s.lname = form.cleaned_data['lname']
            s.age = calc_age(form.cleaned_data['dateofbirth'])
            s.entry_date = form.cleaned_data['entrydate']
            s.dateofbirth = form.cleaned_data['dateofbirth']
            s.noshotrecord = form.cleaned_data['noshotrecord']
            s.exempt_rel = form.cleaned_data['exempt_rel']
            s.exempt_med = form.cleaned_data['exempt_med']
            s.dtap1 = form.cleaned_data['dtap1']
            s.dtap2 = form.cleaned_data['dtap2']
            s.dtap3 = form.cleaned_data['dtap3']
            s.dtap4 = form.cleaned_data['dtap4']
            s.polio1 = form.cleaned_data['polio1']
            s.polio2 = form.cleaned_data['polio2']
            s.polio3 = form.cleaned_data['polio3']
            s.hib = form.cleaned_data['hib']
            s.hepb1 = form.cleaned_data['hepb1']
            s.hepb2 = form.cleaned_data['hepb2']
            s.hepb3 = form.cleaned_data['hepb3']
            s.mmr1 = form.cleaned_data['mmr1']
            s.varicella1 = form.cleaned_data['varicella1']
            s.pe = form.cleaned_data['pe']
            s.tb = form.cleaned_data['tb']
            s.notes = form.cleaned_data['notes']
            if 'Drop' in request.POST:
                s.facility_id = None
                s.save()
                return HttpResponseRedirect(reverse('reportinput:complete'))
            s.facility_id = f.pk
            s.save()
            if s.dtap1:
                s.dtap2 = s.dtap1
                s.save()
            if s.dtap2:
                s.dtap3 = s.dtap2
                s.save()
            if s.dtap3:
                s.dtap4 = s.dtap3
                s.save()
            if s.polio1:
                s.polio2 = s.polio1
                s.save()
            if s.polio2:
                s.polio3 = s.polio2
                s.save()
            if s.hepb1:
                s.hepb2 = s.hepb1
                s.save()
            if s.hepb2:
                s.hepb3 = s.hepb2
                s.save()
            s.save()
            rep.save()
            rep.student_set.add(s)
            return HttpResponseRedirect(reverse('reportinput:complete'))
    return render(request,'reportinput/studentupdate12a.html', {'form':form, 's':student, 'f':f})


@login_required
def landing12a(request):
    personid = request.session['personpk']
    p = Person.objects.get(pk = personid)
    if p.role_id == 1:
        f = Facility.objects.get(pk = request.session['inputid'])
    else:
        f = Facility.objects.get(pk = p.facility_id)
    if request.method == 'POST':
        form = PreKInfo(request.POST)
        if form.is_valid():
            f.under_19_months = form.cleaned_data['under19']
            f.over_19_months = form.cleaned_data['over19']
            f.total_prek = form.cleaned_data['under19'] + form.cleaned_data['over19']
            if form.cleaned_data['students'] == 0:
                if f.is_only_pre_k:
                    f.allimmune = True
                f.save()
                return HttpResponseRedirect(reverse('complete'))
            else:
                f.allimmune = False
                f.count = f.count + form.cleaned_data['students']
                f.save()
                request.session['students'] = form.cleaned_data['students']
                return HttpResponseRedirect(reverse('reportinput:epi12a'))
    else:
        form = PreKInfo(initial={'under19':f.under_19_months,'over19':f.over_19_months})
    return  render(request,'reportinput/landing12a.html',{'form':form})

@login_required
def landing12b(request):
    personid = request.session['personpk']
    p = Person.objects.get(pk = personid)
    if p.role_id == 1:
        f = Facility.objects.get(pk = request.session['inputid'])
    else:
        f = Facility.objects.get(pk = p.facility_id)
    if request.method == 'POST':
        form = SchoolInfo(request.POST)
        if form.is_valid():
            kinder_enroll = form.cleaned_data['kinder_enroll']
            lowest_grade = Enrollment.objects.get(name = form.cleaned_data['lowest_grade'])
            highest_grade = Enrollment.objects.get(name = form.cleaned_data['highest_grade'])
            other_enroll = form.cleaned_data['other_enroll']
            students = form.cleaned_data['students_to_input']
            seventh_grade_enroll = form.cleaned_data['seventh_grade_enroll']
            f.seventh_grade_enroll = seventh_grade_enroll
            f.lowest_grade_id = lowest_grade.pk
            f.highest_grade_id = highest_grade.pk
            f.other_enroll = other_enroll
            if kinder_enroll is not None:
                f.kinder_enroll = kinder_enroll
                f.total_enrolled = other_enroll + kinder_enroll
            else:
                f.total_enrolled = other_enroll
            if students == 0:
                f.allimmune = True
                f.save()
                return HttpResponseRedirect(reverse('reportinput:complete'))
            else:
                f.allimmune = False
                f.count = f.count + students
                f.save()
                request.session['students'] = students
                return HttpResponseRedirect(reverse('reportinput:epi12b'))
    else:
        form = SchoolInfo(initial={'lowest_grade':f.lowest_grade,'highest_grade':f.highest_grade, 'kinder_enroll':f.kinder_enroll, 'other_enroll':f.other_enroll, 'seventh_grade_enroll':f.seventh_grade_enroll})
    return  render(request,'reportinput/landing12b.html',{'form':form, 'f':f,})

@login_required
def complete(request):
    return render(request, 'reportinput/complete.html')

