# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20160331_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='publication_date',
            new_name='created_time',
        ),
    ]
