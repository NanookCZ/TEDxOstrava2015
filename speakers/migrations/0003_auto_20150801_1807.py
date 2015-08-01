# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20150801_0555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='speaker_photo',
        ),
        migrations.AddField(
            model_name='speaker',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='speaker_photo', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='added_by',
            field=models.ForeignKey(verbose_name='User', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='interests',
            field=models.CharField(max_length=100, null=True, verbose_name='interests', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='position',
            field=models.CharField(max_length=50, null=True, verbose_name='position', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='published',
            field=models.BooleanField(default=False, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='share_message',
            field=models.CharField(default='Nov\xfd re\u010dn\xedk', max_length=25, verbose_name='share_message'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speaker_city',
            field=models.CharField(max_length=50, null=True, verbose_name='speaker_city', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='speaker_country',
            field=models.CharField(max_length=50, null=True, verbose_name='speaker_country', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='talk_name',
            field=models.CharField(max_length=25, null=True, verbose_name='talk_name', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
    ]
