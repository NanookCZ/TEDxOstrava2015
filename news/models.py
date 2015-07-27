#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from speakers.models import Speaker


class Type(models.Model):
	title = models.CharField(max_length = 50)
	icon = models.ImageField(upload_to = 'images/', blank = True, null = True)

	def __str__(self):
		return u'self.title'

class News(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField()
	link = models.URLField(null = True, blank = True)
	speaker = models.ForeignKey(Speaker, blank = True, null = True)
	author = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	publication_date = models.DateField(null = True, blank = True)
	active = models.BooleanField(default = True)
	is_published = models.BooleanField(default = False)
	news_image = models.ImageField(upload_to='images/', blank = True, null = True)
	main_news = models.BooleanField(default = False)
	news_type = models.ForeignKey(Type)

	def __str__(self):
		return u'self.title'

	class Meta:
		verbose_name_plural = 'news'