from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
	code = models.CharField(_("code"), max_length = 5, default = 'EN')
	name = models.CharField(_("name"), max_length = 50, default = 'English')

	class Meta:
		verbose_name = _('Language')
		verbose_name_plural = _('Languages')

	def __unicode__(self):
		return "%s" %(self.code)

class Menu(models.Model):
	title = models.CharField(_('title'), max_length = 55, blank = True, null = True)
	title_en = models.CharField(_('title_en'), max_length = 55, blank = True, null = True)
	unique_key = models.SlugField(unique = True, blank = True, null = True)
	icon = CloudinaryField('image', blank = True, null = True)
	active = models.BooleanField(default = True)
	order = models.IntegerField(blank = True, null = True)

	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menu'

	def __unicode__(self):
		return "%s" %(self.title_en)

class Image(models.Model):
	image_title = models.CharField(_('title'), max_length = 55, blank = True, null = True)
	image = CloudinaryField('image', blank = True, null = True)
	round_image = models.URLField(blank = True, null = True)
	active = models.BooleanField(default = True)



	def create_url(self, *args, **kwargs):
		if self.image:
			return "%s%s%s" %('image/upload/w_100,h_100,c_fill,g_face,r_max/', self.image, '.png')

	def image_thumb(self):
		return '<img src="http://res.cloudinary.com/hydqixw1j/image/upload/v1441136781/%s.png" width="100" height="100" />' % (self.image)
	image_thumb.allow_tags = True

	def __unicode__(self):
		return "%s" %(self.image_title)


	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images'


class MPNSDevice(models.Model):
	name = models.CharField(max_length = 255, blank = True, null  = True)
	is_active = models.BooleanField(default = True)
	user = models.ForeignKey(User, blank = True, null = True)
	device_id = models.CharField(max_length = 255, blank = True, null  = True)
	registration_id = models.CharField(max_length = 255, blank = True, null  = True)

	def __unicode__(self):
		return "%s" %(self.name)

	class Meta:
		verbose_name = 'MPNS device'
		verbose_name_plural = 'MPNS devices'
