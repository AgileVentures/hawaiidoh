# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinput', '0004_pastreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastreport',
            name='age',
        ),
        migrations.AlterField(
            model_name='pastreport',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.RemoveField(
            model_name='pastreport',
            name='report',
        ),
        migrations.AddField(
            model_name='pastreport',
            name='report',
            field=models.ForeignKey(to='reportinput.Report', null=True),
        ),
        migrations.RemoveField(
            model_name='pastreport',
            name='student',
        ),
        migrations.AddField(
            model_name='pastreport',
            name='student',
            field=models.ForeignKey(to='reportinput.Student', null=True),
        ),
    ]
