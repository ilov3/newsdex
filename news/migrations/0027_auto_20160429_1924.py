# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_tweet_words'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='created_at',
            new_name='created_time',
        ),
    ]