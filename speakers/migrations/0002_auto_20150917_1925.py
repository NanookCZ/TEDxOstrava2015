# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='first_name',
            field=models.CharField(max_length=225, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='last_name',
            field=models.CharField(max_length=225, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='position',
            field=models.CharField(help_text='Job position of the speaker', max_length=50, null=True, verbose_name='position', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='twitter_url',
            field=models.CharField(help_text='Twitter of the speaker', max_length=50, null=True, blank=True),
        ),
    ]
