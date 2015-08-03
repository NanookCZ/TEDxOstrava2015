from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse
from rest_framework.reverse import reverse as api_reverse
from events.models import Event, Theme
from speakers.models import Speaker
from news.models import News, Type
from partners.models import Partner
from tedx.models import TEDx, AboutApp
from mobile_settings.models import Menu

DOMAIN_NAME = 'https://tedxostrava.herokuapp.com'
@api_view(["GET"])
def tedx_api_home(request):
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
			"count" : Menu.obojects.all().count(),
			"url" : DOMAIN_NAME + api_reverse("menu_list_api")
		},


	}


	return RestResponse(data)