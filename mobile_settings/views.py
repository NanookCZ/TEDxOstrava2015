from .serializers import MenuSerializer, MPNSDeviceSerializer
from .models import Menu, Language
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class MenuListAPIView(generics.ListAPIView):
	queryset = Menu.objects.filter(active = True)
	serializer_class = MenuSerializer
	paginate_by = 10

class MPNSDeviceAPIView(generics.ListAPIView):
	queryset = Menu.objects.all()
	serializer_class = MPNSDeviceSerializer
	paginate_by = 10



