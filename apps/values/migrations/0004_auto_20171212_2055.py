# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0003_auto_20171122_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='properties_string',
            field=models.CharField(blank=True, max_length=100, verbose_name='Batch Code'),
        ),
    ]