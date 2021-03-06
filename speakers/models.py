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
from mobile_settings.models import Language, Image
from cloudinary.utils import cloudinary_url



SHARE_MESSAGE = u'Share...'
class Speaker(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"), default = 1)
	first_name = models.CharField(_('first_name'), max_length = 225)
	last_name = models.CharField(_('last_name'), max_length = 225)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)	
	published = models.BooleanField(_('published'), default = False)
	interests = models.CharField(_('interests'), max_length = 100, blank = True, null = True)
	description = models.TextField(_('description'))
	twitter_url = models.CharField(max_length = 50, blank = True, null = True, help_text="Twitter of the speaker")
	share_message = models.CharField(_('share_message'), max_length = 25, default = SHARE_MESSAGE)
	position = models.CharField(_('position'), max_length = 50, blank = True, null = True, help_text = "Job position of the speaker")
	speaker_photo = models.ForeignKey(Image, blank = True, null = True)
	speaker_city = models.CharField(_('speaker_city'), max_length = 50, blank = True, null = True)
	speaker_country = models.CharField(_('speaker_country'), max_length = 50, blank = True, null = True)
	added_by = models.ForeignKey(User, verbose_name=_("User"), blank = True, null = True)

	def __unicode__(self):
		return "%s %s" %(self.first_name, self.last_name)



	

	class Meta:
		verbose_name = _('Speaker')
		verbose_name_plural = _('Speakers')

