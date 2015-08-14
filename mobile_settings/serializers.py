from .models import Menu
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
			'icon',
			'active',

		]

