from .serializers import SpeakerSerializer
from django.shortcuts import render, get_object_or_404
from .models import Speaker
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class SpeakerListAPIView(generics.ListAPIView):
	queryset = Speaker.objects.filter(active = True, published = True)
	serializer_class = SpeakerSerializer
	paginate_by = 10

class SpeakerDetailAPIView(generics.RetrieveAPIView):
	queryset = Speaker.objects.filter(active = True)
	serializer_class = SpeakerSerializer

	def get_object(self, *args, **kwargs):
		id = self.kwargs.pop('id')
		obj = get_object_or_404(Speaker, id = id)
		return obj
