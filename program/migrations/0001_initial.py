# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', markupfield.fields.MarkupField(null=True, rendered_field=True, blank=True)),
                ('description_markup_type', models.CharField(default=None, max_length=30, blank=True, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST')])),
                ('_description_rendered', models.TextField(null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SlotKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot_name', models.CharField(max_length=50)),
                ('schedule', models.ForeignKey(to='program.Schedule')),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='kind',
            field=models.ForeignKey(to='program.SlotKind'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='section',
            field=models.OneToOneField(to='program.Section'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='section',
            field=models.ForeignKey(to='program.Section'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='slot',
            field=models.OneToOneField(null=True, blank=True, to='program.Slot'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='speakers',
            field=models.ManyToManyField(to='speakers.Speaker', null=True, blank=True),
        ),
    ]
