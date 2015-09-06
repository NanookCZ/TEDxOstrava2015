
from django.conf.urls import include, url
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from events.views import ThemeListAPIView, EventListAPIView, ThemeListEAPIView, EventListEAPIView
from partners.views import PartnerListAPIView
from speakers.views import SpeakerListAPIView, SpeakerDetailAPIView, SpeakerListEAPIView, SpeakerDetailEAPIView
from tedx.views import TEDxListAPIView, AboutAppListAPIView, AboutAppListEAPIView
from news.views import NewsListAPIView, TypeListAPIView, NewsDetailAPIView, NewsListEAPIView, TypeListEAPIView, NewsDetailEAPIView
from mobile_settings.views import MenuListAPIView, MPNSDeviceAPIView, MPNSDeviceCreateAPIView
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns
from push_notifications.api.rest_framework import APNSDeviceViewSet, GCMDeviceViewSet



router = routers.DefaultRouter()
router.register(r'device/apns', APNSDeviceViewSet)
router.register(r'device/gcm', GCMDeviceViewSet)


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^push/', include(router.urls)),
    url(r'^push/device/mpns', MPNSDeviceAPIView.as_view(), name='mpns_list_api'),
    url(r'^push/device/mpns/create', MPNSDeviceCreateAPIView.as_view(), name='mpns_new_api'),
    url(r'^$', RedirectView.as_view(url='admin/', permanent=False), name='index'),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/cs/$', 'tedxostrava.views.tedx_api_home_czech', name="api_home"),
    url(r'^api/cs/events', EventListAPIView.as_view(), name='event_list_api'),
    url(r'^api/cs/partners', PartnerListAPIView.as_view(), name='partner_list_api'),
    url(r'^api/cs/speakers/$', SpeakerListAPIView.as_view(), name='speaker_list_api'),
    url(r'^api/cs/speakers/(?P<id>\d+)/', SpeakerDetailAPIView.as_view(), name='speaker_detail_api'),
    url(r'^api/cs/news/$', NewsListAPIView.as_view(), name='news_list_api'),
    url(r'^api/cs/news/(?P<id>\d+)/', NewsDetailAPIView.as_view(), name='news_detail_api'),
    url(r'^api/cs/types/', TypeListAPIView.as_view(), name='type_list_api'),
    url(r'^api/cs/events/themes', ThemeListAPIView.as_view(), name='theme_list_api'),
    url(r'^api/cs/tedx', TEDxListAPIView.as_view(), name='tedx_list_api'),
    url(r'^api/cs/about', AboutAppListAPIView.as_view(), name='about_list_api'),
    url(r'^api/cs/menu', MenuListAPIView.as_view(), name='menu_list_api'),
    url(r'^api/en/$', 'tedxostrava.views.tedx_api_home_english', name="api_home"),
    url(r'^api/en/events', EventListEAPIView.as_view(), name='event_list_api_e'),
    url(r'^api/en/speakers/$', SpeakerListEAPIView.as_view(), name='speaker_list_api_e'),
    url(r'^api/en/speakers/(?P<id>\d+)/', SpeakerDetailEAPIView.as_view(), name='speaker_detail_api_e'),
    url(r'^api/en/news/$', NewsListEAPIView.as_view(), name='news_list_api_e'),
    url(r'^api/en/news/(?P<id>\d+)/', NewsDetailEAPIView.as_view(), name='news_detail_api_e'),
    url(r'^api/en/types/', TypeListEAPIView.as_view(), name='type_list_api_e'),
    url(r'^api/en/events/themes', ThemeListEAPIView.as_view(), name='theme_list_api_e'),
    url(r'^api/en/about', AboutAppListEAPIView.as_view(), name='about_list_api_e'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
)

