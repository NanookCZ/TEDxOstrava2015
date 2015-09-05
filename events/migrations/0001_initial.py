# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile_settings', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('event_start', models.DateField(null=True, verbose_name='event_start', blank=True)),
                ('event_end', models.DateField(null=True, verbose_name='event_end', blank=True)),
                ('event_start_time', models.CharField(max_length=50, null=True, verbose_name='event_start_time', blank=True)),
                ('event_end_time', models.CharField(max_length=50, null=True, verbose_name='event_end_time', blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('about_ted', models.TextField(null=True, verbose_name='about_ted', blank=True)),
                ('street_address', models.CharField(max_length=50, null=True, verbose_name='street_address', blank=True)),
                ('street_number', models.CharField(max_length=10, null=True, verbose_name='street_number', blank=True)),
                ('city', models.CharField(max_length=25, verbose_name='city')),
                ('state', models.CharField(max_length=25, verbose_name='state')),
                ('zip_code', models.CharField(max_length=10, null=True, verbose_name='zip_code', blank=True)),
                ('latitude', models.CharField(max_length=10, null=True, blank=True)),
                ('longtitude', models.CharField(max_length=10, null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('facebook_url', models.CharField(max_length=50, null=True, blank=True)),
                ('twitter_url', models.CharField(max_length=50, null=True, blank=True)),
                ('share_message', models.CharField(default='Share...', max_length=50, verbose_name='share_message')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('banner', models.ForeignKey(blank=True, to='mobile_settings.Image', null=True)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_theme',
            field=models.ForeignKey(verbose_name='Theme', blank=True, to='events.Theme', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hosted_by',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(to='partners.Partner', null=True, verbose_name='Partner', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, verbose_name='Speaker', blank=True),
        ),
    ]
