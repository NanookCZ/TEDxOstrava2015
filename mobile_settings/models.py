from __future__ import unicode_literals
from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext_lazy as _
from events.models import Language 

class Menu(models.Model):
	title = models.CharField(_('title'), max_length = 50)
	icon = CloudinaryField('image', blank = True, null = True)
	active = models.BooleanField(default = True)
	language = models.ForeignKey(Language, _('language'), blank = True, null = True)

	def __unicode__(self):
		return "%s" %(self.title)

	class Meta:
		verbose_name = _('Menu')
		verbose_name_plural = _('Menu')