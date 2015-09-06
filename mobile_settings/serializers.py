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

		]


		
class ImageSerializer(serializers.HyperlinkedModelSerializer):
	round_image = serializers.CharField(source = 'create_url', read_only = True)
	class Meta:
		model = Image 
		fields = [
			'id',
			'image',
			'round_image',
		]

class MPNSDeviceUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	lookup_field = 'id'

class MPNSDeviceSerializer(serializers.HyperlinkedModelSerializer):
	id = MPNSDeviceUrlHyperlinkedIdentityField(view_name = 'mpns_detail_api', lookup_field = 'id')
	class Meta:
		model = MPNSDevice

class MPNSDeviceCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = MPNSDevice


