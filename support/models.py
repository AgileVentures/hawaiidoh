from django.db import models
from register import models as p

# Create your models here.
class Status(models.Model):
    id = models.AutoField(primary_key=True)
    statustype = models.CharField(max_length=20)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.statustype

class Supportrequest(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(p.Person)
    status = models.ForeignKey('Status')
    description = models.CharField(max_length=255)
    opendate = models.DateField()
    closedate = models.DateField(null = True, blank=True)

    class Meta:
        db_table = 'supportrequest'