# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportinput', '0005_auto_20151212_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastreport',
            name='id',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
        ),
    ]
