from django.contrib import admin
from .models import Event, Theme



admin.site.register(Event)
admin.site.register(Theme, ThemeAdmin)
# Register your models here.
