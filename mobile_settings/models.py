from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
	code = models.CharField(_("code"), max_length = 5)
	name = models.CharField(_("name"), max_length = 50, default = 'English')

	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'

	def __unicode__(self):
		return "%s" %(self.code)

class Menu(models.Model):
	language = models.ForeignKey("Language", blank = True, null = True, verbose_name=_("Language"))
	title = models.CharField(_('title'), max_length = 55)
	icon = CloudinaryField('image', blank = True, null = True)
	active = models.BooleanField(default = True)

	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menu'

	def __unicode__(self):
		return "%s" %(self.title)

