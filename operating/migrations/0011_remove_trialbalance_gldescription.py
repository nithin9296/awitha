# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-17 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0010_auto_20180312_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trialbalance',
            name='gldescription',
        ),
    ]
