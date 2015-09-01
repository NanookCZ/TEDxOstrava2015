from django.contrib import admin
from .models import Menu, Language, Image

admin.site.register(Language)
# Register your models here.
admin.site.register(Menu)

class ImageAdmin(admin.ModelAdmin):
	fields = ('image', 'active',)
	

admin.site.register(Image, ImageAdmin)