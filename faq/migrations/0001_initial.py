# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='faq.Category')),
            ],
            options={
                'db_table': 'faq',
            },
        ),
    ]
