# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.IntegerField(),
        ),
    ]
