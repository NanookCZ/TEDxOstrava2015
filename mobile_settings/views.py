from .serializers import MenuSerializer
from .models import Menu
from rest_framework import generics,  permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class MenuListAPIView(generics.ListAPIView):
	queryset = Menu.objects.filter(active = True, language = 'CS')
	serializer_class = MenuSerializer
	paginate_by = 10