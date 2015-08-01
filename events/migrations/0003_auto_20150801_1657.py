# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150801_0555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='event',
            name='language',
            field=models.ForeignKey(to_field='language', blank=True, to='events.Language', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='about_ted',
            field=models.TextField(null=True, verbose_name='about_ted', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=25, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end',
            field=models.DateField(help_text='End of the event.', null=True, verbose_name='event_end', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.CharField(help_text='End time of the event.', max_length=50, null=True, verbose_name='event_end_time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start',
            field=models.DateField(help_text='Start of the event.', null=True, verbose_name='event_start', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.CharField(help_text='Start time of the event.', max_length=50, null=True, verbose_name='event_start_time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_theme',
            field=models.ForeignKey(to_field='event_theme', blank=True, to='events.Theme', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='facebook_url',
            field=models.CharField(max_length=50, null=True, verbose_name='facebook_url', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='hosted_by'),
        ),
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.CharField(max_length=10, null=True, verbose_name='latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longtitude',
            field=models.CharField(max_length=10, null=True, verbose_name='longtitude', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(db_constraint='partners', null=True, to='partners.Partner', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='share_message',
            field=models.CharField(default='TEDxOstrava - Novinky', max_length=50, verbose_name='share_message'),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(db_constraint='speakers', null=True, to='speakers.Speaker', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(max_length=25, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='event',
            name='street_address',
            field=models.CharField(max_length=50, null=True, verbose_name='street_address', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='street_number',
            field=models.CharField(max_length=10, null=True, verbose_name='street_number', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='event',
            name='twitter_url',
            field=models.CharField(max_length=50, null=True, verbose_name='twitter_url', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='zip_code',
            field=models.CharField(max_length=10, null=True, verbose_name='zip_code', blank=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=5, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=16, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='language',
            field=models.ForeignKey(to_field='language', blank=True, to='events.Language', null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
    ]
