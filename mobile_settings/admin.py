from django.contrib import admin
from .models import Menu, Language

admin.site.register(Language)
# Register your models here.
admin.site.register(Menu)