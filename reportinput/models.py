from __future__ import unicode_literals
from django.db import models
from register import models as info
# Create your models here.

class Student(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50,null=True, blank=True)
    lname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    entry_date = models.DateField()
    enrollment = models.ForeignKey(info.Enrollment, default=1)
    notes = models.CharField(max_length=255, null=True,blank=True)
    noshotrecord = models.BooleanField(default = 0)
    exempt_rel = models.BooleanField(default=0)
    exempt_med = models.BooleanField(default=0)
    dtap1 = models.BooleanField(default=0)
    dtap2 = models.BooleanField(default=0)
    dtap3 = models.BooleanField(default=0)
    dtap4 = models.BooleanField(default=0)
    dtap5 = models.BooleanField(default=0)
    polio1 = models.BooleanField(default=0)
    polio2 = models.BooleanField(default=0)
    polio3 = models.BooleanField(default=0)
    polio4 = models.BooleanField(default=0)
    hib = models.BooleanField(default=0)
    hepb1 = models.BooleanField(default=0)
    hepb2 = models.BooleanField(default=0)
    hepb3 = models.BooleanField(default=0)
    mmr1 = models.BooleanField(default=0)
    mmr2 = models.BooleanField(default=0)
    varicella1 = models.BooleanField(default=0)
    varicella2 = models.BooleanField(default=0)
    pe = models.BooleanField(default=0)
    tb = models.BooleanField(default=0)
    uptodate = models.BooleanField(default=0)
    facility = models.ForeignKey(info.Facility, null=True)
    report = models.ManyToManyField('Report')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return '{} {}'.format(self.fname, self.lname)

class Report(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    person = models.ForeignKey(info.Person)
    facility = models.ForeignKey(info.Facility)
    entrydate = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=0)

    class Meta:
        db_table = 'report'

    def __str__(self):
        return '{} id: {}'.format(str(self.entrydate), str(self.id))