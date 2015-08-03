from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
 
class YourAppConfig(AppConfig):
    name = 'mobile_settings'
    verbose_name = _('Mobile settings')