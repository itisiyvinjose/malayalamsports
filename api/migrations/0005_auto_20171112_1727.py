# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_matchplayer_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='home_page_display_order',
            new_name='display_order',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_date_time',
        ),
        migrations.RemoveField(
            model_name='news',
            name='should_display_on_home_page',
        ),
        migrations.AddField(
            model_name='news',
            name='news_tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
