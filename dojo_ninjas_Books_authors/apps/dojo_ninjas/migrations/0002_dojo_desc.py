# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='default', max_length=255),
        ),
    ]