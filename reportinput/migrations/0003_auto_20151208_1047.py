# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinput', '0002_pastreportdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastreportdata',
            name='report',
        ),
        migrations.RemoveField(
            model_name='pastreportdata',
            name='student',
        ),
        migrations.DeleteModel(
            name='PastReportData',
        ),
    ]
