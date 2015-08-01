
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
#from events.models import Language 


class TEDx(models.Model):
	#language = models.ForeignKey(Language, blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	description = models.TextField(_('description'), blank = True, null = True)
	website = models.URLField(_('website'), null = True, blank = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)
	is_published = models.BooleanField(default = False)
	tedx_logo = CloudinaryField(_('tedx_logo'), 'image', blank = True, null = True)
	event_start = models.DateField(_('event_start'), blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('TEDx')
		verbose_name_plural = _('TEDx')


class AboutApp(models.Model):
	#language = models.ForeignKey(Language, blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	description = models.TextField(_('description'))
	website = models.URLField(_('website'), null = True, blank = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)
	logo = CloudinaryField(_('logo'), 'image', blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('About app')
		verbose_name_plural = _('About app')

