from .serializers import ThemeSerializer, EventSerializer
from .models import Event, Theme
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class ThemeListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = Theme.objects.filter(active = True, language = language)
	serializer_class = ThemeSerializer
	paginate_by = 10

class EventListAPIView(generics.ListAPIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permissions_classes = [permissions.IsAuthenticated, ]
	language = Language.objects.get(code = 'CS')
	queryset = Event.objects.filter(active = True, language = language)
	serializer_class = EventSerializer
	paginate_by = 10


