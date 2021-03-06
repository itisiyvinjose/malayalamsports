# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 04:04
from __future__ import unicode_literals

import api.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FootballMatchCommentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_play_time_status', models.CharField(blank=True, choices=[('FIRST_HALF', 'FIRST_HALF'), ('SECOND_HALF', 'FIRST_HALF'), ('EXTRA_TIME', 'EXTRA TIME'), ('INJURY_TIME', 'INJURY_TIME')], max_length=200, null=True)),
                ('commentary_heading', models.TextField(blank=True, null=True)),
                ('commentary_content', models.TextField()),
                ('is_key_event', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FootBallMatchDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('match_starting_date', models.DateField(blank=True, db_index=True, null=True)),
                ('match_finishing_date', models.DateField(blank=True, null=True)),
                ('match_starting_time', models.TimeField(blank=True, null=True)),
                ('match_finishing_time', models.TimeField(blank=True, null=True)),
                ('match_status', models.CharField(choices=[('UPCOMING', 'MATCH_STATUS'), ('STARTED', 'STARTED'), ('FINISHED', 'FINISHED'), ('POSTPONED', 'POSTPONED'), ('DELAYED', 'DELAYED'), ('DRAW', 'DRAW')], db_index=True, max_length=200)),
                ('match_status_text', models.CharField(blank=True, max_length=200, null=True)),
                ('match_facts', models.TextField(blank=True, null=True)),
                ('match_description', models.TextField(blank=True, null=True)),
                ('venue', models.TextField()),
                ('postponed_date', models.DateField(blank=True, null=True)),
                ('postponed_time', models.TimeField(blank=True, null=True)),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], max_length=200)),
                ('team_one_score', models.IntegerField(default=0)),
                ('team_two_score', models.IntegerField(default=0)),
                ('should_show_on_home_page', models.BooleanField(default=False)),
                ('identifier', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
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
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('jersey_number', models.IntegerField(blank=True, null=True)),
                ('player_role', models.CharField(choices=[('CAPTAIN', 'CAPTAIN'), ('VICE_CAPTAIN', 'VICE_CAPTION'), ('GOAL_KEEPER', 'GOAL_KEEPER'), ('NORMAL', 'NORMAL')], default='NORMAL', max_length=200)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='api.FootBallMatchDetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200, unique=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('starting_date', models.DateField(blank=True, null=True)),
                ('ending_date', models.DateField(blank=True, null=True)),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], db_index=True, max_length=200)),
            ],
            options={
                'ordering': ('display_name',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news_date', models.DateField(db_index=True)),
                ('content', models.TextField()),
                ('source', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('news_tags', models.TextField(blank=True, null=True)),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], max_length=200)),
                ('is_trending', models.BooleanField(default=False)),
                ('trend_scale', models.IntegerField(default=0)),
                ('number_of_likes', models.IntegerField(default=0)),
                ('number_of_dislikes', models.IntegerField(default=0)),
                ('number_of_views', models.IntegerField(default=0)),
                ('display_order', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.get_news_image_path)),
                ('identifier', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='NewsRelationsShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_index', models.IntegerField(default=0)),
                ('common_tags', models.TextField(default='[]')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.News')),
                ('related_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.News')),
            ],
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('tag_name',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], db_index=True, max_length=200)),
                ('biography', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SportsMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('match_starting_date', models.DateField(db_index=True)),
                ('match_starting_time', models.TimeField()),
                ('match_finishing_date', models.DateField()),
                ('match_finishing_time', models.TimeField()),
                ('status', models.CharField(choices=[('UPCOMING', 'MATCH_STATUS'), ('STARTED', 'STARTED'), ('FINISHED', 'FINISHED'), ('POSTPONED', 'POSTPONED'), ('DELAYED', 'DELAYED'), ('DRAW', 'DRAW')], db_index=True, max_length=200)),
                ('match_facts', models.TextField(null=True)),
                ('match_description', models.TextField()),
                ('venue', models.TextField()),
                ('postponed_date', models.DateField()),
                ('postponed_time', models.TimeField()),
                ('concise_summary_text', models.TextField()),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], db_index=True, max_length=200)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='SportsTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('sport', models.CharField(choices=[('FOOTBALL', 'FOOTBALL')], db_index=True, max_length=200)),
                ('team_identifier', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('display_name',),
            },
        ),
        migrations.AddField(
            model_name='sportsmatch',
            name='team_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='sportsmatch',
            name='team_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='sportsmatch',
            name='team_won',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='news',
            name='related_news',
            field=models.ManyToManyField(blank=True, related_name='_news_related_news_+', through='api.NewsRelationsShip', to='api.News'),
        ),
        migrations.AddField(
            model_name='news',
            name='related_tags',
            field=models.ManyToManyField(blank=True, related_name='_news_related_tags_+', to='api.NewsTag'),
        ),
        migrations.AddField(
            model_name='footballmatchdetails',
            name='match_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='api.MatchSeries'),
        ),
        migrations.AddField(
            model_name='footballmatchdetails',
            name='team_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='footballmatchdetails',
            name='team_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='footballmatchdetails',
            name='team_won',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.SportsTeam'),
        ),
        migrations.AddField(
            model_name='footballmatchcommentary',
            name='football_match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaries', to='api.FootBallMatchDetails'),
        ),
        migrations.AlterUniqueTogether(
            name='newsrelationsship',
            unique_together=set([('news', 'related_news')]),
        ),
    ]
