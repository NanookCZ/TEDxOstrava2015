# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('website', models.URLField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('logo', models.ImageField(null=True, upload_to='images/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TEDx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=False)),
                ('tedx_logo', models.ImageField(null=True, upload_to='images/', blank=True)),
                ('event_start', models.DateField(help_text='Start of the event.', null=True, blank=True)),
            ],
        ),
    ]
