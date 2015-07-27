from django.contrib import admin
from .models import News, Type

class NewsAdmin(admin.ModelAdmin):
    date_hiearchy = 'publication_date'
    list_display = ('title', 'news_type', 'active', 'is_published', 'publication_date')
    

admin.site.register(News, NewsAdmin)
admin.site.register(Type)