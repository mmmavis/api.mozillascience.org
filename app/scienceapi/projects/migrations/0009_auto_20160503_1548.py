# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160430_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='scienctific_benefits',
            new_name='scientific_benefits',
        ),
    ]
