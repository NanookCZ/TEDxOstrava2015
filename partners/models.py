#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Partner(models.Model):
	title = models.CharField(max_length = 100)
	created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
	active = models.BooleanField(default = True)	
	partner_logo = models.ImageField(upload_to='images/', blank = True, null = True)
	partner_website = models.URLField(blank = True, null = True)

	def __str__(self):
		return "%s" %(self.title)