# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_type_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='language',
        ),
    ]
