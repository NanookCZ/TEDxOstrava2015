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
from mobile_settings.models import Language, Image 

class Theme(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"), default = 1)
	title = models.CharField(_('title'), max_length = 50)
	description = models.TextField(_('description'), blank = True, null = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	active = models.BooleanField(_('active'), default = True)
	banner = models.ForeignKey(Image, blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _("Theme")
		verbose_name_plural = _("Themes")


SHARE_MESSAGE = 'Share...'
class Event(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, verbose_name=_("Language"), default = 1)
	title = models.CharField(_('title'), max_length = 50)
	event_start = models.DateField(_('event_start'), blank = True, null = True)
	event_end = models.DateField(_('event_end'), blank = True, null = True)
	event_start_time = models.CharField(_('event_start_time'), max_length = 50, blank = True, null = True)
	event_end_time = models.CharField(_('event_end_time'), max_length = 50, blank = True, null = True)
	hosted_by = models.ForeignKey(User, verbose_name=_("User"))
	description = models.TextField(_('description'))
	about_ted = models.TextField(_('about_ted'), blank = True, null = True)
	street_address = models.CharField(_('street_address'), max_length = 50, null = True, blank = True)
	street_number = models.CharField(_('street_number'), max_length = 10, null = True, blank = True)
	city = models.CharField(_('city'), max_length = 25)
	state = models.CharField(_('state'), max_length = 25)
	zip_code = models.CharField(_('zip_code'), max_length = 10, null = True, blank = True)
	latitude = models.CharField(max_length = 10, null = True, blank = True)
	longtitude = models.CharField(max_length = 10, null = True, blank = True)
	created_date = models.DateTimeField(_('created_date'), auto_now_add = True, auto_now = False)
	updated_date = models.DateTimeField(_('updated_date'), auto_now_add = False, auto_now = True)
	event_theme = models.ForeignKey(Theme, blank = True, null = True, verbose_name=_("Theme"))
	active = models.BooleanField(_('active'), default = True)
	speakers = models.ManyToManyField(Speaker, blank = True, null = True, verbose_name=_("Speaker"))
	partners = models.ManyToManyField(Partner, blank = True, null = True, verbose_name=_("Partner"))
	share_message = models.CharField(_('share_message'), max_length = 50, default = SHARE_MESSAGE)

	def __unicode__(self):
		return "%s" %(self.title)


	class Meta:
		verbose_name = _("Event")
		verbose_name_plural = _("Events")