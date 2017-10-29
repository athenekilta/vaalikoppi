# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-29 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=50)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=50)),
                ('is_open', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='voting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaalikoppi.Voting'),
        ),
    ]
