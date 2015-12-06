# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'enrollment',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('has_pre_k', models.BooleanField(default=0)),
                ('is_only_pre_k', models.BooleanField(default=0)),
                ('phone', models.BigIntegerField()),
                ('fax', models.BigIntegerField(null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('under_19_months', models.IntegerField(default=0, null=True, blank=True)),
                ('over_19_months', models.IntegerField(default=0, null=True, blank=True)),
                ('total_prek', models.IntegerField(default=0, null=True, blank=True)),
                ('seventh_grade_enroll', models.IntegerField(default=0, null=True, blank=True)),
                ('kinder_enroll', models.IntegerField(default=0, null=True, blank=True)),
                ('other_enroll', models.IntegerField(default=0, null=True, blank=True)),
                ('total_enrolled', models.IntegerField(default=0, null=True, blank=True)),
                ('allimmune', models.BooleanField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('compliant', models.BooleanField(default=0)),
                ('district', models.ForeignKey(blank=True, to='register.District', null=True)),
                ('highest_grade', models.ForeignKey(related_name='highest', blank=True, to='register.Enrollment', null=True)),
                ('lowest_grade', models.ForeignKey(related_name='lowest', blank=True, to='register.Enrollment', null=True)),
            ],
            options={
                'db_table': 'facility',
            },
        ),
        migrations.CreateModel(
            name='Island',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'island',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50, null=True, blank=True)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('fax', models.BigIntegerField(null=True, blank=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.ForeignKey(to='register.User'),
        ),
        migrations.AddField(
            model_name='person',
            name='facility',
            field=models.ForeignKey(blank=True, to='register.Facility', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(to='register.Role'),
        ),
        migrations.AddField(
            model_name='district',
            name='island',
            field=models.ForeignKey(blank=True, to='register.Island', null=True),
        ),
    ]
