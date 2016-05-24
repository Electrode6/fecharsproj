# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-19 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0009_auto_20160519_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterprimaryclassweapons',
            name='classWeapon',
        ),
        migrations.AddField(
            model_name='characterprimaryclassweapons',
            name='weapon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pyfeck.Weapon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='characterprimaryclassweapons',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.Character'),
        ),
    ]