# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_auto_20150917_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
        migrations.AlterField(
            model_name='slotkind',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True),
        ),
    ]
