# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
