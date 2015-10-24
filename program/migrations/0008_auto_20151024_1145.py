# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_presentation_presentation_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentation',
            options={'verbose_name': 'Speaker', 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Schedule', 'verbose_name_plural': 'Schedule'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.AlterModelOptions(
            name='slot',
            options={'verbose_name': 'Slot', 'verbose_name_plural': 'Slots'},
        ),
        migrations.AlterModelOptions(
            name='slotkind',
            options={'verbose_name': 'Slot Kind', 'verbose_name_plural': 'Slot Kinds'},
        ),
        migrations.AlterField(
            model_name='presentation',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='description',
            field=markupfield.fields.MarkupField(rendered_field=True, null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='end',
            field=models.TimeField(null=True, verbose_name='end', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='presentation_language',
            field=models.CharField(max_length=100, null=True, verbose_name='presentation_language', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='start',
            field=models.TimeField(null=True, verbose_name='start', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='ted_talk_video',
            field=models.URLField(null=True, verbose_name='ted_talk_video', blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='section',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(help_text='Section name, i.e. TEDx Talk, Worskhops,...', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='end',
            field=models.TimeField(verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='start',
            field=models.TimeField(verbose_name='start'),
        ),
        migrations.AlterField(
            model_name='slotkind',
            name='language',
            field=models.ForeignKey(default=1, blank=True, to='mobile_settings.Language', null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='slotkind',
            name='slot_name',
            field=models.CharField(help_text='Sloat name - i. e. Talk, Lunch, Break, ..', max_length=150, verbose_name='slot_name'),
        ),
    ]
