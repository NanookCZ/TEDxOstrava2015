# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('published', models.BooleanField(default=False)),
                ('interests', models.CharField(max_length=100, null=True, blank=True)),
                ('talk_name', models.CharField(max_length=25, null=True, blank=True)),
                ('description', models.TextField()),
                ('twitter_url', models.CharField(max_length=50, null=True, blank=True)),
                ('share_message', models.CharField(default='Nov\xfd re\u010dn\xedk', max_length=25)),
                ('position', models.CharField(max_length=50, null=True, blank=True)),
                ('speaker_photo', models.ImageField(null=True, upload_to='images/', blank=True)),
                ('speaker_city', models.CharField(max_length=50, null=True, blank=True)),
                ('speaker_country', models.CharField(max_length=50, null=True, blank=True)),
                ('added_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
