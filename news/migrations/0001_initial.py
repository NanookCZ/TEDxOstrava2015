# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('link', models.URLField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=False)),
                ('news_image', models.ImageField(null=True, upload_to='images/', blank=True)),
                ('main_news', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('icon', models.ImageField(null=True, upload_to='images/', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_type',
            field=models.ForeignKey(to='news.Type'),
        ),
        migrations.AddField(
            model_name='news',
            name='speaker',
            field=models.ForeignKey(blank=True, to='speakers.Speaker', null=True),
        ),
    ]
