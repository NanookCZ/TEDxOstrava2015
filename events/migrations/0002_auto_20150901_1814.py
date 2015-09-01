# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
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
            field=models.DateField(null=True, verbose_name='event_end', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.CharField(max_length=50, null=True, verbose_name='event_end_time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start',
            field=models.DateField(null=True, verbose_name='event_start', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.CharField(max_length=50, null=True, verbose_name='event_start_time', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_theme',
            field=models.ForeignKey(verbose_name='Theme', blank=True, to='events.Theme', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosted_by',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(to='partners.Partner', null=True, verbose_name='Partner', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='share_message',
            field=models.CharField(default='Share...', max_length=50, verbose_name='share_message'),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, verbose_name='Speaker', blank=True),
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
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='zip_code',
            field=models.CharField(max_length=10, null=True, verbose_name='zip_code', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='banner',
            field=models.ForeignKey(blank=True, to='mobile_settings.Image', null=True),
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
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
    ]
