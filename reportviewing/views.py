from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from register.models import Facility, Person, Enrollment, Island, District
from reportinput.models import Student, Report
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django import forms
from itertools import chain
import datetime
import csv
# Create your views here.

@login_required
def removefromreport(request, student_id):
    student = Student.objects.get(pk = student_id)
    report = Report.objects.filter(student__id = student.pk).get(complete=False)
    if request.method =='POST':
        if 'confirm' in request.POST:
            report.student_set.remove(student)
            return HttpResponseRedirect(reverse('reportinput:complete'))
        else:
            return HttpResponseRedirect(reverse('reportviewing:reportbydate'))
    return render(request, 'reportviewing/confirm.html')

@login_required
def reportsbydate(request):
    p = Person.objects.get(pk = request.session['personpk'])
    try:
        r = Report.objects.filter(facility_id=p.facility_id)
    except (Report.DoesNotExist):
        return render(request, 'reportviewing/reportsbydate.html',{'error_message': "No reports for this facility",})
    return render(request,'reportviewing/reportsbydate.html',{'reports':r,})

@login_required
def schoolreport(request, report_id):
    r = Report.objects.get(pk = report_id)
    s = Student.objects.filter(report__id=r.pk)
    p = Person.objects.get(pk = request.session['personpk'])
    f = Facility.objects.get(pk = p.facility_id)
    if s:
        filterobject = s[0]
        if request.method == 'POST':
            if 'confirm' in request.POST:
                r.complete = True
                r.save()
                f.compliant = True
                f.save()
                return HttpResponseRedirect(reverse('login:landingpage'))
            else:
                if filterobject.enrollment_id == 1:
                    return HttpResponseRedirect(reverse('reportviewing:csva', args=(r.pk,)))
                else:
                    return HttpResponseRedirect(reverse('reportviewing:csvb', args=(r.pk,)))
    return render(request, 'reportviewing/schoolreport.html', {'students':s, 'report':r})

@login_required
def createschoolcsva(request, report_id):
    r = Report.objects.get(pk = report_id)
    students = Student.objects.filter(report__id=r.pk)
    f = Facility.objects.get(pk = r.facility_id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prekmaster.csv"'

    writer = csv.writer(response)
    writer.writerow([f.name,
                     'Report ID:',
                     r.id,
                     datetime.datetime.today()])
    writer.writerow(['Student ID',
                     'Name',
                     'Date of Birth',
                     'Age',
                     'No Shot Record',
                     'Medically Exempt',
                     'Religiously Exempt',
                     'Dtap 1',
                     'Dtap 2',
                     'Dtap 3',
                     'Dtap 4',
                     'Polio 1',
                     'Polio 2',
                     'Polio 3',
                     'Hib',
                     'HepB 1',
                     'HepB 2',
                     'HepB 3',
                     'MMR 1',
                     'Varicella 1',
                     'PE',
                     'TB',
                     'Notes'])
    for student in students:
        name = ''
        if student.mname == '':
            name = '{} {}'.format(student.fname, student.lname)
        else:
            name = '{} {} {}'.format(student.fname, student.mname, student.lname)
        writer.writerow([student.id,
                         name,
                         student.dateofbirth,
                         student.age,
                         student.noshotrecord,
                         student.exempt_med,
                         student.exempt_rel,
                         student.dtap1,
                         student.dtap2,
                         student.dtap3,
                         student.dtap4,
                         student.polio1,
                         student.polio2,
                         student.polio3,
                         student.hib,
                         student.hepb1,
                         student.hepb2,
                         student.hepb3,
                         student.mmr1,
                         student.varicella1,
                         student.pe,
                         student.tb,
                         student.notes])


    return response

@login_required
def createschoolcsvb(request, report_id):
    r = Report.objects.get(pk = report_id)
    students = Student.objects.filter(report__id=r.pk)
    f = Facility.objects.get(pk = r.facility_id)

    students = students.exclude(enrollment_id = 1)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gradeschoolmaster.csv"'

    writer = csv.writer(response)
    writer.writerow([f.name,
                     'Report ID:',
                     r.id,
                     datetime.datetime.today()])
    writer.writerow(['Student ID',
                     'Name',
                     'Date of Birth',
                     'Grade',
                     'No Shot Record',
                     'Medically Exempt',
                     'Religiously Exempt',
                     'Dtap 1',
                     'Dtap 2',
                     'Dtap 3',
                     'Dtap 4',
                     'Dtap 5',
                     'Polio 1',
                     'Polio 2',
                     'Polio 3',
                     'Polio 4',
                     'HepB 1',
                     'HepB 2',
                     'HepB 3',
                     'MMR 1',
                     'MMR 2',
                     'Varicella 1',
                     'Varicella 2',
                     'PE',
                     'TB',
                     'Notes'])
    for student in students:
        name = ''
        if student.mname == '':
            name = '{} {}'.format(student.fname, student.lname)
        else:
            name = '{} {} {}'.format(student.fname, student.mname, student.lname)
        writer.writerow([student.id,
                         name,
                         student.dateofbirth,
                         student.enrollment,
                         student.noshotrecord,
                         student.exempt_med,
                         student.exempt_rel,
                         student.dtap1,
                         student.dtap2,
                         student.dtap3,
                         student.dtap4,
                         student.dtap5,
                         student.polio1,
                         student.polio2,
                         student.polio3,
                         student.polio4,
                         student.hepb1,
                         student.hepb2,
                         student.hepb3,
                         student.mmr1,
                         student.mmr2,
                         student.varicella1,
                         student.varicella2,
                         student.pe,
                         student.tb,
                         student.notes])
    return response

@login_required
def createmasterlist12a(request):
    students = Student.objects.filter(enrollment_id = 1).order_by('facility')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prekmaster.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student ID',
                     'Name',
                     'Date of Birth',
                     'School',
                     'Age',
                     'No Shot Record',
                     'Medically Exempt',
                     'Religiously Exempt',
                     'Dtap 1',
                     'Dtap 2',
                     'Dtap 3',
                     'Dtap 4',
                     'Polio 1',
                     'Polio 2',
                     'Polio 3',
                     'Hib',
                     'HepB 1',
                     'HepB 2',
                     'HepB 3',
                     'MMR 1',
                     'Varicella 1',
                     'PE',
                     'TB',
                     'Notes'])
    for student in students:
        name = ''
        if student.mname == '':
            name = '{} {}'.format(student.fname, student.lname)
        else:
            name = '{} {} {}'.format(student.fname, student.mname, student.lname)
        writer.writerow([student.id,
                         name,
                         student.dateofbirth,
                         student.facility,
                         student.age,
                         student.noshotrecord,
                         student.exempt_med,
                         student.exempt_rel,
                         student.dtap1,
                         student.dtap2,
                         student.dtap3,
                         student.dtap4,
                         student.polio1,
                         student.polio2,
                         student.polio3,
                         student.hib,
                         student.hepb1,
                         student.hepb2,
                         student.hepb3,
                         student.mmr1,
                         student.varicella1,
                         student.pe,
                         student.tb,
                         student.notes])
    return response

@login_required
def createmasterlist12b(request):
    students = Student.objects.exclude(enrollment_id = 1).order_by('facility')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gradeschoolmaster.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student ID',
                     'Name',
                     'Date of Birth',
                     'School',
                     'Grade',
                     'No Shot Record',
                     'Medically Exempt',
                     'Religiously Exempt',
                     'Dtap 1',
                     'Dtap 2',
                     'Dtap 3',
                     'Dtap 4',
                     'Dtap 5',
                     'Polio 1',
                     'Polio 2',
                     'Polio 3',
                     'Polio 4',
                     'HepB 1',
                     'HepB 2',
                     'HepB 3',
                     'MMR 1',
                     'MMR 2',
                     'Varicella 1',
                     'Varicella 2',
                     'PE',
                     'TB',
                     'Notes'])
    for student in students:
        name = ''
        if student.mname == '':
            name = '{} {}'.format(student.fname, student.lname)
        else:
            name = '{} {} {}'.format(student.fname, student.mname, student.lname)
        writer.writerow([student.id,
                         name,
                         student.dateofbirth,
                         student.facility,
                         student.enrollment,
                         student.noshotrecord,
                         student.exempt_med,
                         student.exempt_rel,
                         student.dtap1,
                         student.dtap2,
                         student.dtap3,
                         student.dtap4,
                         student.dtap5,
                         student.polio1,
                         student.polio2,
                         student.polio3,
                         student.polio4,
                         student.hepb1,
                         student.hepb2,
                         student.hepb3,
                         student.mmr1,
                         student.mmr2,
                         student.varicella1,
                         student.varicella2,
                         student.pe,
                         student.tb,
                         student.notes])
    return response

@login_required
def listofstudents(request):
    f = Facility.objects.get(pk = request.session['inputid'])
    type = request.session['type']
    s = Student.objects.all()
    if type == 1 and f.pk > 1:
        s = Student.objects.filter(facility_id = f.pk, exempt_med=True).order_by('lname').order_by('fname')
    if type == 2 and f.pk > 1:
        s = Student.objects.filter(facility_id = f.pk, exempt_rel=True).order_by('lname').order_by('fname')
    if type == 3 and f.pk > 1:
        s = Student.objects.filter(facility_id = f.pk).filter(Q(exempt_med=True)| Q(exempt_rel=True)).order_by('lname').order_by('fname')
    if type == 4 and f.pk > 1:
        s = Student.objects.exclude(uptodate = True).filter(facility_id = f.pk)
    return render(request, 'reportviewing/students.html',{'s':s, 'n':type,'f':f})

@login_required
def studentfilter(request):
    form = StudentFilter()
    person = Person.objects.get(pk = request.session['personpk'])
    if person.role_id == 1:
        students = Student.objects.all().order_by('facility')
    else:
        students = Student.objects.filter(facility_id=person.facility_id).order_by('lname')

    if request.session['lname'] != 'all':
        if person.role_id == 1:
            students = Student.objects.filter(lname__icontains=request.session['lname']).order_by('facility')
        else:
            students = Student.objects.filter(facility_id = person.facility_id).filter(lname__icontains=request.session['lname']).order_by('facility').order_by('lname')

    if request.method=='POST':
        if 'remove' in request.POST:
            return HttpResponseRedirect(reverse('reportviewing:removehighest'))
        form = StudentFilter(request.POST)
        if 'import' in request.POST:
            return HttpResponseRedirect(reverse('reportviewing:importview'))
        if form.is_valid():
            if form.cleaned_data['lname'] is None:
                request.session['lname'] = 'all'
            else:
                request.session['lname'] = form.cleaned_data['lname']
        return HttpResponseRedirect(reverse('reportviewing:studentfilter'))
    paginator = Paginator(students, 6)
    page = request.GET.get('page')
    try:
        children = paginator.page(page)
    except PageNotAnInteger:
        children = paginator.page(1)
    except EmptyPage:
        children = paginator.page(paginator.num_pages)
    return render(request, 'reportviewing/studentlist.html', {'students':children,'form':form,})

@login_required
def epi12apdf(request):
    file = open('static/login/EPI12A.pdf', 'rb')
    content = file.read()
    file.close()
    response = HttpResponse(content, content_type ='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "epi12a.pdf"'
    return response

@login_required
def epi12bpdf(request):
    file = open('static/login/EPI12B.pdf', 'rb')
    content = file.read()
    file.close()
    response = HttpResponse(content, content_type ='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "epi12b.pdf"'
    return response

class StudentFilter(forms.Form):

    lname = forms.CharField(max_length=50, required=False)
    id = forms.IntegerField(required=False)

@login_required()
def importstudent(request, student_id):
    s = Student.objects.get(pk = student_id)
    p = Person.objects.get(pk = request.session['personpk'])
    s.facility_id = p.facility_id
    s.save()
    f = Facility.objects.get(pk = s.facility_id)
    if not f.compliant:
        r = Report.objects.filter(facility_id=f.id).get(complete=False)
    else:
        r = Report(person_id=p.pk, facility_id=p.facility_id,entrydate=datetime.datetime.today())
        r.save()
        f.compliant = False
        f.save()
        students = Student.objects.filter(facility_id = s.facility_id)
        for student in students:
            student.report.add(r)
    s.report.add(r)
    s.save()
    return HttpResponseRedirect(reverse('reportviewing:studentfilter'))

@login_required
def importview(request):
    s = None
    form = StudentFilter()
    if request.method == 'POST':
        form = StudentFilter(request.POST)
        if form.is_valid():
            s = Student.objects.filter(Q(pk = form.cleaned_data['id']) & (Q(facility_id = 1) | Q(facility_id = None)))
            if s:
                s = s[0]
    return render(request, 'reportviewing/import.html', {'s':s, 'form':form})

@login_required
def removehighestgrade(request):
    person = Person.objects.get(pk = request.session['personpk'])
    facility = Facility.objects.get(pk = person.facility_id)
    highestgrade = facility.highest_grade_id
    students = Student.objects.filter(Q(facility_id=facility.pk) & Q(enrollment_id=highestgrade))
    if students:
        for s in students:
            s.facility_id = None
            s.save()
    return HttpResponseRedirect(reverse('reportviewing:studentfilter'))