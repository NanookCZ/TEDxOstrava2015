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
from mobile_settings.models import Language, Image

class Type(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"),default = 'EN')
	title = models.CharField(_('title'), max_length = 50)
	icon = CloudinaryField('image', blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('Type')
		verbose_name_plural = _('Types')

class News(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"), default = 'EN')
	title = models.CharField(_('title'), max_length = 250)
	description = models.TextField(_('description'))
	link = models.URLField(null = True, blank = True)
	speaker = models.ForeignKey(Speaker, verbose_name=_("Speaker"), blank = True, null = True)
	author = models.ForeignKey(User, verbose_name=_("User"))
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	publication_date = models.DateField(_('publication_date'), null = True, blank = True)
	active = models.BooleanField(_('active'), default = True)
	is_published = models.BooleanField(_('is_published'), default = False)
	news_image = models.ForeignKey(Image, blank = True, null = True)
	main_news = models.BooleanField(_('main_news'), default = False)
	news_type = models.ForeignKey(Type, verbose_name=_("Type"))

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('News')
		verbose_name_plural = _('News')