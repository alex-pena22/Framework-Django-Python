# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-24 06:05
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180622_0233'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('validator', django.db.models.manager.Manager()),
            ],
        ),
    ]