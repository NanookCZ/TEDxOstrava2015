#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField


SHARE_MESSAGE = u'Nový rečník'
class Speaker(models.Model):
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)	
	published = models.BooleanField(default = False)
	interests = models.CharField(max_length = 100, blank = True, null = True)
	talk_name = models.CharField(max_length = 25, blank = True, null = True)
	description = models.TextField()
	twitter_url = models.CharField(max_length = 50, blank = True, null = True)
	share_message = models.CharField(max_length = 25, default = SHARE_MESSAGE)
	position = models.CharField(max_length = 50, blank = True, null = True)
	speaker_photo = CloudinaryField('image', blank = True, null = True)
	speaker_city = models.CharField(max_length = 50, blank = True, null = True)
	speaker_country = models.CharField(max_length = 50, blank = True, null = True)
	added_by = models.ForeignKey(User, blank = True, null = True)

	def __unicode__(self):
		return "%s %s" %(self.first_name, self.last_name)

