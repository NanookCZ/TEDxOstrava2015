#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from speakers.models import Speaker
from partners.models import Partner
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
	code = models.CharField(max_length=5)
	name = models.CharField(max_length=16)

	def __unicode__(self):
		return "%s" %(self.code)

class Theme(models.Model):
	#language = models.ForeignKey(Language, blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	description = models.TextField(_('description'), blank = True, null = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)
	banner = CloudinaryField('image', blank = True, null = True)

	class Meta:
		verbose_name = _('theme')
		verbose_name_plural = _('themes')

	def __unicode__(self):
		return "%s" %(self.title)



SHARE_MESSAGE = 'TEDxOstrava - Novinky'
class Event(models.Model):
	#language = models.ForeignKey("Language", blank = True, null = True)
	title = models.CharField(_('title'), max_length = 50)
	event_start = models.DateField(_('event_start'), blank = True, null = True, help_text='Start of the event.')
	event_end = models.DateField(_('event_end'), blank = True, null = True, help_text='End of the event.')
	event_start_time = models.CharField(_('event_start_time'), max_length = 50, blank = True, null = True, help_text='Start time of the event.')
	event_end_time = models.CharField(_('event_end_time'), max_length = 50, blank = True, null = True, help_text='End time of the event.')
	hosted_by = models.ForeignKey(User, _('hosted_by'))
	description = models.TextField(_('description'))
	about_ted = models.TextField(_('about_ted'), blank = True, null = True)
	street_address = models.CharField(_('street_address'), max_length = 50, null = True, blank = True)
	street_number = models.CharField(_('street_number'), max_length = 10, null = True, blank = True)
	city = models.CharField(_('city'), max_length = 25)
	state = models.CharField(_('state'), max_length = 25)
	zip_code = models.CharField(_('zip_code'), max_length = 10, null = True, blank = True)
	latitude = models.CharField(_('latitude'), max_length = 10, null = True, blank = True)
	longtitude = models.CharField(_('longtitude'), max_length = 10, null = True, blank = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	event_theme = models.ForeignKey(Theme, _('event_theme'), blank = True, null = True)
	active = models.BooleanField(_('active'), default = True)
	speakers = models.ManyToManyField(Speaker, _('speakers'), blank = True, null = True)
	partners = models.ManyToManyField(Partner, _('partners'), blank = True, null = True)
	facebook_url = models.CharField(_('facebook_url'), max_length = 50, blank = True, null = True)
	twitter_url = models.CharField(_('twitter_url'), max_length = 50, blank = True, null = True)
	share_message = models.CharField(_('share_message'), max_length = 50, default = SHARE_MESSAGE)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Events'


