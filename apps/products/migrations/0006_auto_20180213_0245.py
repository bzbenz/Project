# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-12 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180208_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_sale',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 13, 2, 45, 44, 689600), verbose_name='Date of Sale'),
        ),
    ]
