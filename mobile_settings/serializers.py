from .models import Menu, Image, MPNSDevice
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MenuSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Menu
		fields = [
			'id',
			'title',
			'title_en',
			'unique_key',
			'icon',
			'active',
			'order',

		]


		
class ImageSerializer(serializers.HyperlinkedModelSerializer):
	round_image = serializers.CharField(source = 'create_url', read_only = True)
	image = serializers.CharField(source = 'speaker_url', read_only = True)
	class Meta:
		model = Image 
		fields = [
			'id',
			'image',
			'round_image',
			#'speaker_image',
		]


class MPNSDeviceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MPNSDevice



