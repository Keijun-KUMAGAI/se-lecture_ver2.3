# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_seminar', models.IntegerField(default=0)),
                ('language_english', models.IntegerField(default=0)),
                ('sport', models.IntegerField(default=0)),
                ('human_basic', models.IntegerField(default=0)),
                ('science_basic_human', models.IntegerField(default=0)),
                ('science_basic_science', models.IntegerField(default=0)),
                ('liberal_human', models.IntegerField(default=0)),
                ('liberal_science', models.IntegerField(default=0)),
                ('liberal_all', models.IntegerField(default=0)),
                ('liberal_free', models.IntegerField(default=0)),
                ('major', models.IntegerField(default=0)),
            ],
        ),
    ]
