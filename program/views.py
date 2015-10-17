from django.shortcuts import render
from .serializers import PresentationSerializer, SlotSerializer
from .models import Presentation, Slot
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class ProgramListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Presentation.objects.filter(active = True, language = language).order_by('slot')
	except:
		pass 
	serializer_class = PresentationSerializer

class SlotListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer

class SlotDetailAPIView(generics.RetrieveAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer