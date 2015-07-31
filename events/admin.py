from django.contrib import admin
from .models import Event, Theme, ThemeI18N
from i18n_model.admin import I18nInlineMixin

class ThemeI18nInline(I18nInlineMixin, admin.StackedInline):
    model = Theme

class ThemeAdmin(admin.ModelAdmin):
	inlines = [ThemeI18nInline]

admin.site.register(Event)
admin.site.register(Theme, ThemeAdmin)
# Register your models here.
