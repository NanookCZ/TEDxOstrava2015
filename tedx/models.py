
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField


class TEDx(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True, null = True)
	website = models.URLField(null = True, blank = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)
	is_published = models.BooleanField(default = False)
	tedx_logo = CloudinaryField('image', blank = True, null = True)
	event_start = models.DateField(blank = True, null = True, help_text='Start of the event.')

	def __unicode__(self):
		return "%s" %(self.title)

class AboutApp(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField()
	website = models.URLField(null = True, blank = True)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)
	logo = CloudinaryField('image', blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

