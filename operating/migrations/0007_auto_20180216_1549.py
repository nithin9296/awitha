# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-16 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0006_auto_20180216_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynetpercentage',
            name='user',
            field=models.CharField(max_length=25),
        ),
    ]
