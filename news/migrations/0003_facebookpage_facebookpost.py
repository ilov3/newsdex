# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-19 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField()),
                ('text', models.TextField()),
                ('post_id', models.CharField(max_length=255)),
                ('parent_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.FacebookPage')),
            ],
        ),
    ]
