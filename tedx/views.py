from .serializers import TEDxSerializer, AboutAppSerializer
from .models import TEDx, AboutApp
from rest_framework import generics
import datetime
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class TEDxListAPIView(generics.ListAPIView):
	queryset = TEDx.objects.filter(active = True, is_published = True, event_start__gte = datetime.datetime.now())
	serializer_class = TEDxSerializer
	

class TEDxListEAPIView(generics.ListAPIView):
	queryset = TEDx.objects.filter(active = True, is_published = True, event_start__gte = datetime.datetime.now())
	serializer_class = TEDxSerializer
	



class AboutAppListAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'CS')
		queryset = AboutApp.objects.filter(active = True, language = language)
	except:
		pass
	serializer_class = AboutAppSerializer
	



class AboutAppListEAPIView(generics.ListAPIView):
	try:
		language = Language.objects.get(code = 'EN')
		queryset = AboutApp.objects.filter(active = True, language = language)
	except:
		pass
	serializer_class = AboutAppSerializer
	