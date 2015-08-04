from .serializers import NewsSerializer, TypeSerializer
from django.shortcuts import render, get_object_or_404
from .models import News, Type
import datetime
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from mobile_settings.models import Language

class TypeListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = Type.objects.all(language = language)
	serializer_class = TypeSerializer
	paginate_by = 10

class NewsListAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = News.objects.filter(active = True, language = language, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer
	paginate_by = 10


class NewsDetailAPIView(generics.RetrieveAPIView):
	language = Language.objects.get(code = 'CS')
	queryset = News.objects.filter(language = language, active = True, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer

	def get_object(self, *args, **kwargs):
		id = self.kwargs.pop('id')
		obj = get_object_or_404(News, id = id)
		return obj

class TypeListEAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = Type.objects.all(language = language)
	serializer_class = TypeSerializer
	paginate_by = 10

class NewsListEAPIView(generics.ListAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = News.objects.filter(language = language, active = True, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer
	paginate_by = 10


class NewsDetailEAPIView(generics.RetrieveAPIView):
	language = Language.objects.get(code = 'EN')
	queryset = News.objects.filter(language = language, active = True, is_published = True, publication_date__lte = datetime.datetime.now())
	serializer_class = NewsSerializer

	def get_object(self, *args, **kwargs):
		id = self.kwargs.pop('id')
		obj = get_object_or_404(News, id = id)
		return obj
