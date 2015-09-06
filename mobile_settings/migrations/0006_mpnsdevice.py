# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile_settings', '0005_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPNSDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('device_id', models.CharField(max_length=255, null=True, blank=True)),
                ('registration_id', models.CharField(max_length=255, null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'MPNS device',
                'verbose_name_plural': 'MPNS devices',
            },
        ),
    ]
