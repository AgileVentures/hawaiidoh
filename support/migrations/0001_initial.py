# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('statustype', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Supportrequest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('opendate', models.DateField()),
                ('closedate', models.DateField(null=True, blank=True)),
                ('person', models.ForeignKey(to='register.Person')),
                ('status', models.ForeignKey(to='support.Status')),
            ],
            options={
                'db_table': 'supportrequest',
            },
        ),
    ]
