from __future__ import unicode_literals
from django.db import models
from events.models import Event
from speakers.models import Speaker
from markupfield.fields import MarkupField
from mobile_settings.models import Language, Image 
from django.core.exceptions import ValidationError

class Section(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1)
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=100, help_text="Section name, i.e. TEDx Talk, Worskhops,...")


	def __unicode__(self):
		return "%s - %s" % (self.event, self.name)

class Schedule(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1)
	section = models.OneToOneField(Section)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s" %(self.section)


class SlotKind(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1)
	schedule = models.ForeignKey(Schedule)
	slot_name = models.CharField(max_length=150, help_text="Sloat name - i. e. Talk, Lunch, Break, ..")

	def __unicode__(self):
		return "%s" %(self.slot_name)


class Slot(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1)
	kind = models.ForeignKey(SlotKind) 
	start = models.TimeField()
	end = models.TimeField()

	def __unicode__(self):
		return "%s" %(self.kind)


def validate_date(date):
	slot_id = Slot._meta.get_field('id')
	slot = Slot.objects.get(id = slot_id)
	if date != slot.start:
		raise ValidationError("Error")

class Presentation(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True, default = 1)
	slot = models.ForeignKey(Slot, null=True, blank=True)
	title = models.CharField(max_length=100)
	start = models.TimeField(blank=True, null = True, validators=[validate_date])
	end = models.TimeField(blank=True, null = True)
	description = MarkupField(blank = True, null = True)
	cover_image = models.ForeignKey(Image, blank = True, null = True)
	speakers = models.ManyToManyField(Speaker, blank=True, null = True)
	ted_talk_video = models.URLField(blank = True, null = True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s" %(self.title)

