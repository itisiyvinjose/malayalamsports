# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 18:33
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_news_thumbnail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestnews',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.get_guest_news_image_path),
        ),
        migrations.AddField(
            model_name='guestnews',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sportsteam',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.get_team_logo_image_path),
        ),
    ]
