# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('link', models.URLField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('publication_date', models.DateField(null=True, verbose_name='publication_date', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('is_published', models.BooleanField(default=False, verbose_name='is_published')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='news_image', blank=True)),
                ('main_news', models.BooleanField(default=False, verbose_name='main_news')),
                ('author', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('icon', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image', blank=True)),
                ('language', models.ForeignKey(verbose_name='Language', blank=True, to='mobile_settings.Language', null=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(verbose_name='Type', to='news.Type'),
        ),
        migrations.AddField(
            model_name='news',
            name='speaker',
            field=models.ForeignKey(verbose_name='Speaker', blank=True, to='speakers.Speaker', null=True),
        ),
    ]
