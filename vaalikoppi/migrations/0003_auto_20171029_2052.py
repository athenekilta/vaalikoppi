# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-29 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaalikoppi', '0002_auto_20171029_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='voting_description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]