from .models import Menu, Image
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class MenuSerializer(serializers.HyperlinkedModelSerializer):
	status_display = serializers.SerializerMethodField('get_status_display')
	class Meta:
		model = Menu
		fields = [
			'id',
			'title',
			'title_en',
			'unique_key',
			'icon',
			'active',
			'status_display',

		]

		def get_status_display(self, obj):
			return obj.get_status_display()

class ImageSerializer(serializers.HyperlinkedModelSerializer):
	round_image = serializers.CharField(source = 'create_url', read_only = True)
	class Meta:
		model = Image 
		fields = [
			'id',
			'image',
			'round_image',
		]