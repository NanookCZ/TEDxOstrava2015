from .serializers import TEDxSerializer, AboutAppSerializer
from .models import TEDx, AboutApp
from rest_framework import generics
import datetime
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class TEDxListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = TEDx.objects.filter(language = language, active = True, is_published = True, event_start__lte = datetime.datetime.now())
	serializer_class = TEDxSerializer
	paginate_by = 10



class AboutAppListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = AboutApp.objects.filter(active = True, language = language)
	serializer_class = AboutAppSerializer
	paginate_by = 10


class TEDxListEAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = TEDx.objects.filter(language = language, active = True, is_published = True, event_start__lte = datetime.datetime.now())
	serializer_class = TEDxSerializer
	paginate_by = 10



class AboutAppListEAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = AboutApp.objects.filter(active = True, language = language)
	serializer_class = AboutAppSerializer
	paginate_by = 10