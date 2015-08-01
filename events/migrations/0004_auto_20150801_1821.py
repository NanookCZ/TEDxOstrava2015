# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedx', '0004_auto_20150801_1821'),
        ('news', '0004_auto_20150801_1821'),
        ('events', '0003_auto_20150801_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='partners',
            field=models.ManyToManyField(to='partners.Partner', null=True, verbose_name='Partner', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, verbose_name='Speaker', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
