# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'theme', 'verbose_name_plural': 'themes'},
        ),
        migrations.AlterField(
            model_name='theme',
            name='banner',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='title',
            field=models.CharField(help_text='This is the theme title', max_length=50, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='theme',
            name='language',
            field=models.ForeignKey(blank=True, to='events.Language', null=True),
        ),
    ]
