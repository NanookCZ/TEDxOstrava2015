from django.shortcuts import render
from .serializers import PresentationSerializer
from .models import Presentation
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class ProgramListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = Presentation.objects.filter(active = True, language = language)
	except:
		pass 
	serializer_class = PresentationSerializer