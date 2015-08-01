# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Theme', 'verbose_name_plural': 'Themes'},
        ),
        migrations.AlterField(
            model_name='event',
            name='about_ted',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end',
            field=models.DateField(help_text='End of the event.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.CharField(help_text='End time of the event.', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start',
            field=models.DateField(help_text='Start of the event.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.CharField(help_text='Start time of the event.', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_theme',
            field=models.ForeignKey(blank=True, to='events.Theme', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='facebook_url',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longtitude',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(to='partners.Partner', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='share_message',
            field=models.CharField(default='TEDxOstrava - Check our news', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='street_address',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='street_number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='twitter_url',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='zip_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='theme',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
