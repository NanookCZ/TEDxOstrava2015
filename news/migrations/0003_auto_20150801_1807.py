# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150801_1807'),
        ('news', '0002_auto_20150801_0555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_image',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='news_image', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='events.Language', null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='language',
            field=models.ForeignKey(verbose_name='Language', blank=True, to='events.Language', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='is_published'),
        ),
        migrations.AlterField(
            model_name='news',
            name='main_news',
            field=models.BooleanField(default=False, verbose_name='main_news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(verbose_name='Type', to='news.Type'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateField(null=True, verbose_name='publication_date', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='speaker',
            field=models.ForeignKey(verbose_name='Speaker', blank=True, to='speakers.Speaker', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_date'),
        ),
        migrations.AlterField(
            model_name='type',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
