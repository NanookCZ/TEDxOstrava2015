from .serializers import PartnerSerializer
from .models import Partner
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class PartnerListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = Partner.objects.filter(active = True, language = language)
	serializer_class = PartnerSerializer
	paginate_by = 10

class PartnerListEAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = Partner.objects.filter(active = True, language = language)
	serializer_class = PartnerSerializer
	paginate_by = 10