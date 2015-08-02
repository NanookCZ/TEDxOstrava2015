# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


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
                ('title', models.CharField(max_length=50)),
                ('event_start', models.DateField(help_text='Start of the event.', null=True, blank=True)),
                ('event_end', models.DateField(help_text='End of the event.', null=True, blank=True)),
                ('event_start_time', models.CharField(help_text='Start time of the event.', max_length=50, null=True, blank=True)),
                ('event_end_time', models.CharField(help_text='End time of the event.', max_length=50, null=True, blank=True)),
                ('description', models.TextField()),
                ('about_ted', models.TextField(null=True, blank=True)),
                ('street_address', models.CharField(max_length=50, null=True, blank=True)),
                ('street_number', models.CharField(max_length=10, null=True, blank=True)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('latitude', models.CharField(max_length=10, null=True, blank=True)),
                ('longtitude', models.CharField(max_length=10, null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('facebook_url', models.CharField(max_length=50, null=True, blank=True)),
                ('twitter_url', models.CharField(max_length=50, null=True, blank=True)),
                ('share_message', models.CharField(default='TEDxOstrava - Check our news', max_length=50)),
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
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('banner', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
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
            field=models.ForeignKey(blank=True, to='events.Theme', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hosted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(to='partners.Partner', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, blank=True),
        ),
    ]
