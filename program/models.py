from __future__ import unicode_literals
from django.db import models
from events.models import Event
from speakers.models import Speaker
from markupfield.fields import MarkupField
from mobile_settings.models import Language, Image 
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Section(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1, verbose_name=_("Language"))
	event = models.ForeignKey(Event)
	name = models.CharField(_('name'), max_length=100, help_text="Section name, i.e. TEDx Talk, Worskhops,...")


	def __unicode__(self):
		return "%s - %s" % (self.event, self.name)

	class Meta:
		verbose_name = _('Section')
		verbose_name_plural = _('Sections')

class Schedule(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1, verbose_name=_("Language"))
	section = models.OneToOneField(Section, related_name='section')
	active = models.BooleanField(_('active'), default=True)

	def __unicode__(self):
		return "%s" %(self.section)

	class Meta:
		verbose_name = _('Schedule')
		verbose_name_plural = _('Schedule')


class SlotKind(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1, verbose_name=_("Language"))
	schedule = models.ForeignKey(Schedule)
	slot_name = models.CharField(_('slot_name'), max_length=150, help_text="Sloat name - i. e. Talk, Lunch, Break, ..")

	def __unicode__(self):
		return "%s" %(self.slot_name)

	class Meta:
		verbose_name = _('Slot Kind')
		verbose_name_plural = _('Slot Kinds')


class Slot(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1, verbose_name=_("Language"))
	kind = models.ForeignKey(SlotKind) 
	start = models.TimeField(_('start'))
	end = models.TimeField(_('end'))

	def __unicode__(self):
		return "%s" %(self.kind)

	def clean(self):
		if self.end <= self.start:
			raise ValidationError(_("End comes before start"))
		super(Slot, self).clean()

	class Meta:
		verbose_name = _('Slot')
		verbose_name_plural = _('Slots')

class Presentation(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1, verbose_name=_("Language"))
	presentation_language = models.CharField(_('presentation_language'), max_length=100, blank = True, null = True)
	slot = models.ForeignKey(Slot, null=True, blank=True)
	title = models.CharField(_('title'), max_length=100)
	start = models.TimeField(_('start'), blank=True, null = True)
	end = models.TimeField(_('end'), blank=True, null = True)
	description = MarkupField(_('description'), blank = True, null = True)
	cover_image = models.ForeignKey(Image, blank = True, null = True)
	speakers = models.ManyToManyField(Speaker, blank=True, null = True)
	ted_talk_video = models.URLField(_('ted_talk_video'), blank = True, null = True)
	active = models.BooleanField(_('active'), default=True)

	def __unicode__(self):
		return "%s" %(self.title)

	def clean(self):
		if self.end <= self.start:
			raise ValidationError(_("End comes before start"))
		super(Presentation, self).clean()

	def clean(self):
		if self.start <= self.slot.start or self.end >= self.slot.end:
			raise ValidationError(_("Time is not in session time interval"))
		super(Presentation, self).clean()

	def get_speaker_count(self):
		return self.speakers.count()

	class Meta:
		verbose_name = _('Speaker')
		verbose_name_plural = _('Speakers')

	


