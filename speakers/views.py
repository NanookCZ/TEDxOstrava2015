from .serializers import SpeakerSerializer
from django.shortcuts import render, get_object_or_404
from .models import Speaker
from rest_framework import generics
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

"""
class SpeakerListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Speaker.objects.filter(active = True, published = True, language = language)
	except:
		speaker = Speaker.objects.create(language = 2)
		speaker.save()
		language = Language.objects.get(code = 'CS')
		queryset = Speaker.objects.filter(active = True, published = True, language = language)
	serializer_class = SpeakerSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('first_name', 'last_name')
	paginate_by = 10

class SpeakerDetailAPIView(generics.RetrieveAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Speaker.objects.filter(active = True, language = language)
	except:
		pass
	serializer_class = SpeakerSerializer

	def get_object(self, *args, **kwargs):
		try:
			id = self.kwargs.pop('id')
			obj = get_object_or_404(Speaker, id = id)
			return obj
		except:
			pass

class SpeakerListEAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Speaker.objects.filter(active = True, published = True, language = language)
	except:
		pass
	serializer_class = SpeakerSerializer
	paginate_by = 10

class SpeakerDetailEAPIView(generics.RetrieveAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Speaker.objects.filter(active = True, language = language)
	except:
		pass
	serializer_class = SpeakerSerializer

	def get_object(self, *args, **kwargs):
		try:
			id = self.kwargs.pop('id')
			obj = get_object_or_404(Speaker, id = id)
			return obj
		except:
			pass
"""
