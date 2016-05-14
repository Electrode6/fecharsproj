# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0012_auto_20160410_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supportlevelavailability',
            options={'verbose_name': 'Support Level Availability', 'verbose_name_plural': 'Support Level Availabilities'},
        ),
        migrations.AddField(
            model_name='character',
            name='generation',
            field=models.IntegerField(choices=[(1, 'Generation One'), (2, 'Generation Two'), (3, 'Generation Three')], default=1),
        ),
    ]
