from .serializers import PartnerSerializer
from .models import Partner
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PartnerListAPIView(generics.ListAPIView):
	queryset = Partner.objects.filter(active = True)
	serializer_class = PartnerSerializer
	paginate_by = 10