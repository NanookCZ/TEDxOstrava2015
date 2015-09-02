from .models import Menu, Image
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .views import Test

class MenuSerializer(serializers.HyperlinkedModelSerializer):
	title = serializers.CharField(source = 'test', read_only = True)
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