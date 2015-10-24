from .models import Section, Schedule, SlotKind, Slot, Presentation
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from speakers.serializers import SpeakerSerializer
from mobile_settings.serializers import ImageSerializer








class PresentationSerializer(serializers.HyperlinkedModelSerializer):
	#slot = SlotSerializer(many = False)
	cover_image = ImageSerializer(many = False)
	speakers = SpeakerSerializer(many = True)
	class Meta:
		model = Presentation
		fields = [
			'id',
			'title',
			'presentation_language',
			'start',
			'end',
			'description',
			#'url',
			#'slot',
			'cover_image',
			'speakers',
			'ted_talk_video',
			'active',
			
		]




class SlotSerializer(serializers.HyperlinkedModelSerializer):
	presentation_set = PresentationSerializer(many = True, read_only = True)
	class Meta:
		model = Slot
		fields = [
			'id',
			#'kind',
			'start',
			'end',
			'presentation_set',

		]

class SlotKindSerializer(serializers.HyperlinkedModelSerializer):
	slot_set = SlotSerializer(many = True, read_only = True)
	class Meta:
		model = SlotKind
		fields = [
			'id',
			'slot_name',
			'slot_set',

		]

		
class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
	slotkind_set = SlotKindSerializer(many = True, read_only = True)
	class Meta:
		model = Schedule
		fields = [
			'id',
			#'section',
			'slotkind_set',

		]




class SectionSerializer(serializers.HyperlinkedModelSerializer):
	schedule_set = ScheduleSerializer(many = True, read_only = True)
	class Meta:
		model = Section 
		fields = [
			'id',
			'name',
			'schedule_set',

		]


