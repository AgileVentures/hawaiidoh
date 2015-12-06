from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

class Faq(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    category = models.ForeignKey('Category')

    class Meta:
        db_table = 'faq'