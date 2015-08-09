from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse
from rest_framework.reverse import reverse as api_reverse
from events.models import Event, Theme
from speakers.models import Speaker
from news.models import News, Type
from partners.models import Partner
from tedx.models import TEDx, AboutApp
from mobile_settings.models import Menu
from django.http import HttpResponse

print(request.META['HTTP_HOST'])



DOMAIN_NAME = request.META['HTTP_HOST']
@api_view(["GET"])
def tedx_api_home_czech(request):
	data = {
		"events" : {
			"count" : Event.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("event_list_api"),
			},
		"themes" : {
			"count" : Theme.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("theme_list_api")
			},
		"speakers" : {
			"count" : Speaker.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("speaker_list_api")
			},
		"news" : {
			"count" : News.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("news_list_api")
			},
		"types" : {
			"count" : Type.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("type_list_api")
			},
		"partners" : {
			"count" : Partner.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("partner_list_api")
			},
		"tedx" : {
			"count" : TEDx.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("tedx_list_api")
			},
		"about" : {
			"count" : AboutApp.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("about_list_api")
			},
		"menu" : {
			"count" : Menu.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("menu_list_api")
		},


	}


	return RestResponse(data)


@api_view(["GET"])
def tedx_api_home_english(request):
	data = {
		"events" : {
			"count" : Event.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("event_list_api_e"),
			},
		"themes" : {
			"count" : Theme.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("theme_list_api_e")
			},
		"speakers" : {
			"count" : Speaker.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("speaker_list_api_e")
			},
		"news" : {
			"count" : News.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("news_list_api_e")
			},
		"types" : {
			"count" : Type.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("type_list_api_e")
			},
		"partners" : {
			"count" : Partner.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("partner_list_api_e")
			},
		"tedx" : {
			"count" : TEDx.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("tedx_list_api_e")
			},
		"about" : {
			"count" : AboutApp.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("about_list_api_e")
			},
		"menu" : {
			"count" : Menu.objects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("menu_list_api_e")
		},


	}


	return RestResponse(data)