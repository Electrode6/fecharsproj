# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0004_auto_20160328_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClassPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_class', to='pyfeck.CharacterClass')),
                ('toClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_class', to='pyfeck.CharacterClass')),
            ],
        ),
        migrations.RemoveField(
            model_name='characterclasscategorypromotion',
            name='fromCategory',
        ),
        migrations.RemoveField(
            model_name='characterclasscategorypromotion',
            name='toCategory',
        ),
        migrations.DeleteModel(
            name='CharacterClassCategoryPromotion',
        ),
    ]