# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0002_auto_20160518_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='currentClass',
        ),
    ]
