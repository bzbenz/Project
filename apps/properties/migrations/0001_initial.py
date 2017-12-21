# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Detail')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]
