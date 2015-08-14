from .models import Event, Theme
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from partners.serializers import PartnerSerializer

from django.contrib.auth.models import User

class UserSerialzer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'email'
		]

class ThemeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Theme
		fields = [
			#'url',
			'id',
			'title',
			'description',
			'banner',

		]

class EventSerializer(serializers.HyperlinkedModelSerializer):
	event_theme = ThemeSerializer(many = False, read_only = True)
	theme_title = serializers.CharField(source = 'event_theme.title', read_only = True)
	theme_banner = serializers.CharField(source = 'event_theme.banner', read_only = True)
	hosted_by = UserSerialzer(many = False, read_only = True)
	partners = PartnerSerializer(many = True, read_only = True)
	class Meta:
		model = Event
		fields = [
			#'url',
			'id',
			'title',
			'event_start',
			'event_end',
			'event_start_time',
			'event_end_time',
			'description',
			'about_ted',
			'street_address',
			'street_number',
			'city',
			'state',
			'zip_code',
			'latitude',
			'longtitude',
			'event_theme',
			'theme_banner',
			'theme_title',
			'active',
			'hosted_by',
			'partners',
			'share_message',
		]