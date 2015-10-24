from django.contrib import admin
from .models import Menu, Language, Image
from django.utils.translation import ugettext_lazy as _

admin.site.register(Language)
# Register your models here.
admin.site.register(Menu)

class ImageAdmin(admin.ModelAdmin):
	fields = (_('image_title'), 'image', 'active', _('image_thumb'))
	readonly_fields = ['image_thumb']
	list_display = ('image_title', 'active', 'image_thumb')
	

admin.site.register(Image, ImageAdmin)