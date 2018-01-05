# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.IntegerField(choices=[(-2, 'Banned'), (-1, 'Expired'), (0, 'Draft'), (1, 'Sale'), (2, 'Booked'), (3, 'Sold')], default=1, verbose_name='Status'),
        ),
    ]
