from django.contrib import admin
from .models import Menu, Language, Image

admin.site.register(Language)
# Register your models here.
admin.site.register(Menu)

class ImageAdmin(admin.ModelAdmin):
	fields = ('image', 'active', 'image_thumb')
	readonly_fields = ['image_thumb']
	

admin.site.register(Image, ImageAdmin)