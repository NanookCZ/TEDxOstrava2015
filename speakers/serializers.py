from .models import Speaker
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class SpeakerUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	lookup_field = 'id'
	


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
	url = SpeakerUrlHyperlinkedIdentityField(view_name = 'speaker_detail_api')
	class Meta:
		model = Speaker
		fields = [
			'id',
			'url',
			'first_name',
			'last_name',
			'active',
			'published',
			'interests',
			'talk_name',
			'description',
			'position',
			'speaker_photo',
			'speaker_city',
			'speaker_country',
			'share_message',
			

		]