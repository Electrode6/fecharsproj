# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfeck', '0011_auto_20160410_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClassCategoryRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromClassCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_Class_Category', to='pyfeck.CharacterClassCategory')),
                ('toClassCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_Class_Category', to='pyfeck.CharacterClassCategory')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependentCharacter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependent_Character', to='pyfeck.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSupportLevelStatBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attackStanceBonus', models.IntegerField()),
                ('guardStanceBonus', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.Character')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.StatCategory')),
            ],
        ),
        migrations.CreateModel(
            name='SupportLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SupportLevelAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sexcategory',
            options={'verbose_name': 'Sex Category', 'verbose_name_plural': 'Sex Categories'},
        ),
        migrations.AddField(
            model_name='characterclassstat',
            name='guardStanceBonus',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supportlevel',
            name='availability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.SupportLevelAvailability'),
        ),
        migrations.AddField(
            model_name='charactersupportlevelstatbonus',
            name='supportLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.SupportLevel'),
        ),
        migrations.AddField(
            model_name='characterrelationship',
            name='supportLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfeck.SupportLevel'),
        ),
        migrations.AddField(
            model_name='characterrelationship',
            name='supportedCharacter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supported_Character', to='pyfeck.Character'),
        ),
        migrations.AddField(
            model_name='characterrelationship',
            name='supportingCharacter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporting_Character', to='pyfeck.Character'),
        ),
    ]
