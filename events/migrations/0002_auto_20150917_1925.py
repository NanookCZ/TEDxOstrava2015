# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='event',
            name='twitter_url',
        ),
    ]
