# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinput', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastReportData',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('notes', models.CharField(max_length=255, null=True, blank=True)),
                ('noshotrecord', models.BooleanField(default=0)),
                ('exempt_rel', models.BooleanField(default=0)),
                ('exempt_med', models.BooleanField(default=0)),
                ('dtap1', models.BooleanField(default=0)),
                ('dtap2', models.BooleanField(default=0)),
                ('dtap3', models.BooleanField(default=0)),
                ('dtap4', models.BooleanField(default=0)),
                ('dtap5', models.BooleanField(default=0)),
                ('polio1', models.BooleanField(default=0)),
                ('polio2', models.BooleanField(default=0)),
                ('polio3', models.BooleanField(default=0)),
                ('polio4', models.BooleanField(default=0)),
                ('hib', models.BooleanField(default=0)),
                ('hepb1', models.BooleanField(default=0)),
                ('hepb2', models.BooleanField(default=0)),
                ('hepb3', models.BooleanField(default=0)),
                ('mmr1', models.BooleanField(default=0)),
                ('mmr2', models.BooleanField(default=0)),
                ('varicella1', models.BooleanField(default=0)),
                ('varicella2', models.BooleanField(default=0)),
                ('pe', models.BooleanField(default=0)),
                ('tb', models.BooleanField(default=0)),
                ('report', models.ManyToManyField(to='reportinput.Report')),
                ('student', models.ManyToManyField(to='reportinput.Student')),
            ],
            options={
                'db_table': 'pastreportdata',
            },
        ),
    ]
