# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20160403_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordsFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtered_word', models.CharField(default='', max_length=255)),
            ],
        ),
    ]