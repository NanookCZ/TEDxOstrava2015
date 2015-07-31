
from django.conf.urls import include, url
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from events.views import ThemeListAPIView, EventListAPIView
from partners.views import PartnerListAPIView
from speakers.views import SpeakerListAPIView, SpeakerDetailAPIView
from tedx.views import TEDxListAPIView, AboutAppListAPIView
from news.views import NewsListAPIView, TypeListAPIView, NewsDetailAPIView
from django.views.generic.base import RedirectView



router = routers.DefaultRouter()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', RedirectView.as_view(url='admin/', permanent=False), name='index'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', 'tedxostrava.views.tedx_api_home', name="api_home"),
    url(r'^api/events', EventListAPIView.as_view(), name='event_list_api'),
    url(r'^api/partners', PartnerListAPIView.as_view(), name='partner_list_api'),
    url(r'^api/speakers/$', SpeakerListAPIView.as_view(), name='speaker_list_api'),
    url(r'^api/speakers/(?P<id>\d+)/', SpeakerDetailAPIView.as_view(), name='speaker_detail_api'),
    url(r'^api/news/$', NewsListAPIView.as_view(), name='news_list_api'),
    url(r'^api/news/(?P<id>\d+)/', NewsDetailAPIView.as_view(), name='news_detail_api'),
    url(r'^api/types/', TypeListAPIView.as_view(), name='type_list_api'),
    url(r'^api/events/themes', ThemeListAPIView.as_view(), name='theme_list_api'),
    url(r'^api/tedx', TEDxListAPIView.as_view(), name='tedx_list_api'),
    url(r'^api/about', AboutAppListAPIView.as_view(), name='about_list_api'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)