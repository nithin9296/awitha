# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-27 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balancesheet',
            old_name='gldescription',
            new_name='gldescriptions',
        ),
    ]
