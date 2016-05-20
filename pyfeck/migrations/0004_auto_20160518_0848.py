# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0003_remove_character_currentclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='primaryClassCategory',
        ),
        migrations.RemoveField(
            model_name='character',
            name='secondaryClassCategory',
        ),
        migrations.AddField(
            model_name='character',
            name='primaryClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='primary_Class', to='pyfeck.CharacterClass', verbose_name='primary class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='secondaryClass',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_Class', to='pyfeck.CharacterClass', verbose_name='secondary class'),
            preserve_default=False,
        ),
    ]
