# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20170604_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', to='practice.Topping'),
        ),
    ]
