# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_auto_20180220_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='popular',
            field=models.IntegerField(default=0),
        ),
    ]
