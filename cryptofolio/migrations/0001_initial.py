# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1024)),
                ('secret', models.CharField(max_length=1024)),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptofolio.Exchange')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('exchangeAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptofolio.ExchangeAccount')),
            ],
        ),
    ]