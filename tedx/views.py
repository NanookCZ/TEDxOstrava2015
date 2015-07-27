from .serializers import TEDxSerializer, AboutAppSerializer
from .models import TEDx, AboutApp
from rest_framework import generics
import datetime
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class TEDxListAPIView(generics.ListAPIView):
	queryset = TEDx.objects.filter(active = True, is_published = True, event_start__lte = datetime.datetime.now())
	serializer_class = TEDxSerializer
	paginate_by = 10



class AboutAppListAPIView(generics.ListAPIView):
	queryset = AboutApp.objects.filter(active = True)
	serializer_class = AboutAppSerializer
	paginate_by = 10
