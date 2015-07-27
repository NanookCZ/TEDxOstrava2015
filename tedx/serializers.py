from .models import TEDx, AboutApp
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class TEDxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TEDx
		fields = [
			'id',
			'title',
			'description',
			'website',
			'active',
			'is_published',
			'tedx_logo',
			'event_start',
			

		]

class AboutAppSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AboutApp
		fields = [
			'id',
			'title',
			'description',
			'website',
			'active',
			'logo',
			

		]