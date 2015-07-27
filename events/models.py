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


class Theme(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True, null = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)
	banner = CloudinaryField('image', blank = True, null = True)

	def __str__(self):
		return "%s" %(self.title)


SHARE_MESSAGE = 'TEDxOstrava - Novinky'
class Event(models.Model):
	title = models.CharField(max_length = 50)
	event_start = models.DateField(blank = True, null = True, help_text='Start of the event.')
	event_end = models.DateField(blank = True, null = True, help_text='End of the event.')
	event_start_time = models.CharField(max_length = 50, blank = True, null = True, help_text='Start time of the event.')
	event_end_time = models.CharField(max_length = 50, blank = True, null = True, help_text='End time of the event.')
	hosted_by = models.ForeignKey(User)
	description = models.TextField()
	about_ted = models.TextField(blank = True, null = True)
	street_address = models.CharField(max_length = 50, null = True, blank = True)
	street_number = models.CharField(max_length = 10, null = True, blank = True)
	city = models.CharField(max_length = 25)
	state = models.CharField(max_length = 25)
	zip_code = models.CharField(max_length = 10, null = True, blank = True)
	latitude = models.CharField(max_length = 10, null = True, blank = True)
	longtitude = models.CharField(max_length = 10, null = True, blank = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	event_theme = models.ForeignKey(Theme, blank = True, null = True)
	active = models.BooleanField(default = True)
	speakers = models.ManyToManyField(Speaker, blank = True, null = True)
	partners = models.ManyToManyField(Partner, blank = True, null = True)
	facebook_url = models.CharField(max_length = 50, blank = True, null = True)
	twitter_url = models.CharField(max_length = 50, blank = True, null = True)
	share_message = models.CharField(max_length = 50, default = SHARE_MESSAGE)

	def __str__(self):
		return "%s" %(self.title)


