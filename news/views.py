from .serializers import NewsSerializer, TypeSerializer
from django.shortcuts import render, get_object_or_404
from .models import News, Type
import datetime
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class TypeListAPIView(generics.ListAPIView):
	queryset = Type.objects.all()
	serializer_class = TypeSerializer
	paginate_by = 10

class NewsListAPIView(generics.ListAPIView):
	queryset = News.objects.filter(active = True, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer
	paginate_by = 10


class NewsDetailAPIView(generics.RetrieveAPIView):
	queryset = News.objects.filter(active = True, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer

	def get_object(self, *args, **kwargs):
		id = self.kwargs.pop('id')
		obj = get_object_or_404(News, id = id)
		return obj
