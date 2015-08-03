from .serializers import SpeakerSerializer
from django.shortcuts import render, get_object_or_404
from .models import Speaker
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class SpeakerListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = Speaker.objects.filter(active = True, published = True, language = language)
	serializer_class = SpeakerSerializer
	paginate_by = 10

class SpeakerDetailAPIView(generics.RetrieveAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = Speaker.objects.filter(active = True, language = language)
	serializer_class = SpeakerSerializer

	def get_object(self, *args, **kwargs):
		id = self.kwargs.pop('id')
		obj = get_object_or_404(Speaker, id = id)
		return obj
