from .models import News, Type
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from speakers.serializers import SpeakerSerializer

class TypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Type
		fields = [
			'id',
			'title',
			'icon',
		
		]

class NewsUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	lookup_field = 'id'

class NewsSerializer(serializers.HyperlinkedModelSerializer):
	url = NewsUrlHyperlinkedIdentityField(view_name = 'news_detail_api')
	speaker = SpeakerSerializer(many = False, read_only = True)
	news_type = TypeSerializer(many = False, read_only = True)
	title = serializers.CharField(source = 'news_type.title', read_only = True)
	icon = serializers.CharField(source = 'news_type.icon', read_only = True)
	class Meta:
		model = News
		fields = [
			'id',
			'title',
			'url',
			'title',
			'description',
			'link',
			'speaker',
			'publication_date',
			'active',
			'is_published',
			'news_image',
			'news_type',
			'title',
			'icon',


]

