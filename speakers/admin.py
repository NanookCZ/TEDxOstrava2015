from django.contrib import admin
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    date_hiearchy = 'published'
    list_display = ('first_name', 'last_name', 'active', 'published')
    

admin.site.register(Speaker, SpeakerAdmin)