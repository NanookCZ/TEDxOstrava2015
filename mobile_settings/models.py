from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from sorl.thumbnail.main import DjangoThumbnail
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
	code = models.CharField(_("code"), max_length = 5)
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

	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menu'

	def __unicode__(self):
		return "%s" %(self.title)

class Image(models.Model):
	image = CloudinaryField('image', blank = True, null = True)
	round_image = models.URLField(blank = True, null = True)
	active = models.BooleanField(default = True)


	def create_url(self, *args, **kwargs):
		if self.image:
			return "%s%s%s" %('image/upload/w_100,h_100,c_fill,g_face,r_max/', self.image, '.png')

	def slide_thumbnail(self):
		if self.image:
			thumb = DjangoThumbnail(self.image)
			return '{img src="%s" /}' % thumb.absolute_url
		return '{img src="/media/img/admin/icon-no.gif" alt="False"}'
	slide_thumbnail.allow_tags = True

	def __unicode__(self):
		return u'Slide: %s - %sx%s' % (self.image)

	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images'


