#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from speakers.models import Speaker
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from events.models import Language 

class Type(models.Model):
	language = models.ForeignKey(Language, _('language'), blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	icon = CloudinaryField('image', blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('Type')
		verbose_name_plural = _('Types')

class News(models.Model):
	language = models.ForeignKey(Language, _('language'), blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	description = models.TextField(_('description'))
	link = models.URLField(null = True, blank = True)
	speaker = models.ForeignKey(Speaker, _('speaker'), blank = True, null = True)
	author = models.ForeignKey(User, _('author'))
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	publication_date = models.DateField(_('publication_date'), null = True, blank = True)
	active = models.BooleanField(_('active'), default = True)
	is_published = models.BooleanField(_('is_published'), default = False)
	news_image = CloudinaryField(_('news_image'), 'image', blank = True, null = True)
	main_news = models.BooleanField(_('main_news'), default = False)
	news_type = models.ForeignKey(Type, _('news_type'))

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('News')
		verbose_name_plural = _('News')