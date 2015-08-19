#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from mobile_settings.models import Language



SHARE_MESSAGE = u'Share...'
class Speaker(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"))
	first_name = models.CharField(_('first_name'), max_length = 25)
	last_name = models.CharField(_('last_name'), max_length = 25)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)	
	published = models.BooleanField(_('published'), default = False)
	interests = models.CharField(_('interests'), max_length = 100, blank = True, null = True)
	talk_name = models.CharField(_('talk_name'), max_length = 25, blank = True, null = True)
	description = models.TextField(_('description'))
	twitter_url = models.CharField(max_length = 50, blank = True, null = True)
	share_message = models.CharField(_('share_message'), max_length = 25, default = SHARE_MESSAGE)
	position = models.CharField(_('position'), max_length = 50, blank = True, null = True)
	speaker_photo = CloudinaryField('image', blank = True, null = True)
	speaker_city = models.CharField(_('speaker_city'), max_length = 50, blank = True, null = True)
	speaker_country = models.CharField(_('speaker_country'), max_length = 50, blank = True, null = True)
	added_by = models.ForeignKey(User, verbose_name=_("User"), blank = True, null = True)

	def __unicode__(self):
		return "%s %s" %(self.first_name, self.last_name)

	def transform_image(self):
		new_image = cloudinary.CloudinaryImage(self.speaker_photo).image(
        width = 90, height = 98, 
        crop = 'fill', gravity = 'face',
        radius = 'max')
        self.speaker_photo = new_image
        self.speaker_photo.save()
        return self.speaker_photo


	class Meta:
		verbose_name = _('Speaker')
		verbose_name_plural = _('Speakers')

