# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150801_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('icon', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('language', models.ForeignKey(to_field='language', blank=True, to='events.Language', null=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
    ]
