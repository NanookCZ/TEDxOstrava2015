from .models import Partner
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Partner
		fields = [
			'id',
			'title',
			'active',
			'partner_logo',
			'partner_website',
		]