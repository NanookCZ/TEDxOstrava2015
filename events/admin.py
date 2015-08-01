from django.contrib import admin
from .models import Event, Theme, Language

admin.site.register(Language)
admin.site.register(Event)
admin.site.register(Theme)
# Register your models here.
