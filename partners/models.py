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


class Partner(models.Model):
	#language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"))
	title = models.CharField(_('title'), max_length = 100)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)	
	partner_logo = CloudinaryField(_('partner_logo'), 'image', blank = True, null = True)
	partner_website = models.URLField(_('partner_website'), blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('Partner')
		verbose_name_plural = _('Partners')