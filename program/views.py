from django.shortcuts import render
from .serializers import PresentationSerializer, SlotSerializer, SectionSerializer, ScheduleSerializer, SlotKindSerializer
from .models import Presentation, Slot, Section, SlotKind
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class ProgramListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Section.objects.filter(language = language)
	except:
		pass 
	serializer_class = SectionSerializer

class SlotListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer

class SlotDetailAPIView(generics.RetrieveAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer


class ProgramListEAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = SlotKind.objects.filter(language = language)
	except:
		pass
	serializer_class = SlotKindSerializer


class SlotListEAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer

class SlotDetailEAPIView(generics.RetrieveAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = Slot.objects.filter(language = language)
	except:
		pass 
	serializer_class = SlotSerializer