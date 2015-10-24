from .serializers import MenuSerializer
from .models import Menu, Language
from rest_framework import generics,  permissions, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class MenuListAPIView(generics.ListAPIView):
	queryset = Menu.objects.filter(active = True).order_by('order')
	serializer_class = MenuSerializer
	paginate_by = 10

class MenuListEAPIView(generics.ListAPIView):
	queryset = Menu.objects.filter(active = True).order_by('order')
	serializer_class = MenuSerializer
	paginate_by = 10



	





