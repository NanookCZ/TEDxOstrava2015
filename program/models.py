from __future__ import unicode_literals
from django.db import models
from events.models import Event
from speakers.models import Speaker
from markupfield.fields import MarkupField
from mobile_settings.models import Language

class Section(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True)
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=100, help_text="Section name, i.e. TEDx Talk, Worskhops,...")


	def __unicode__(self):
		return "%s - %s" % (self.event, self.name)

class Schedule(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True)
	section = models.OneToOneField(Section)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s" %(self.section)


class SlotKind(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True)
	schedule = models.ForeignKey(Schedule)
	slot_name = models.CharField(max_length=150, help_text="Sloat name - i. e. Talk, Lunch, Break, ..")

	def __unicode__(self):
		return "%s" %(self.slot_name)


class Slot(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True)
	kind = models.ForeignKey(SlotKind) 
	start = models.TimeField()
	end = models.TimeField()

	def __unicode__(self):
		return "%s" %(self.kind)

class Presentation(models.Model):
	language = models.ForeignKey(Language, blank = True, null = True)
	slot = models.OneToOneField(Slot, null=True, blank=True)
	title = models.CharField(max_length=100)
	description = MarkupField(blank = True, null = True)
	speakers = models.ManyToManyField(Speaker, blank=True, null = True)
	section = models.ForeignKey(Section)

	def __unicode__(self):
		return "%s - %s" %(self.title, self.speaker)

