# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171112_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news_date', models.DateField(db_index=True)),
                ('content', models.TextField()),
                ('source', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], max_length=200)),
                ('number_of_likes', models.IntegerField(default=0)),
                ('number_of_dislikes', models.IntegerField(default=0)),
                ('display_order', models.IntegerField(default=0)),
                ('is_admin_approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
