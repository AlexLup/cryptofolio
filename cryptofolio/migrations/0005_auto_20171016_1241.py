# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptofolio', '0004_auto_20171016_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='fiat',
            field=models.CharField(default='USD', max_length=10),
        ),
    ]
