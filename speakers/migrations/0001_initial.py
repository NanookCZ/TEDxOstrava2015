# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last_name')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('interests', models.CharField(max_length=100, null=True, verbose_name='interests', blank=True)),
                ('talk_name', models.CharField(max_length=25, null=True, verbose_name='talk_name', blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('twitter_url', models.CharField(max_length=50, null=True, blank=True)),
                ('share_message', models.CharField(default='Share...', max_length=25, verbose_name='share_message')),
                ('position', models.CharField(max_length=50, null=True, verbose_name='position', blank=True)),
                ('speaker_city', models.CharField(max_length=50, null=True, verbose_name='speaker_city', blank=True)),
                ('speaker_country', models.CharField(max_length=50, null=True, verbose_name='speaker_country', blank=True)),
                ('added_by', models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
    ]
