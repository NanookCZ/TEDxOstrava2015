from django.contrib import admin
from .models import Partner

class PartnerAdmin(admin.ModelAdmin):
    date_hiearchy = 'updated_date'
    list_display = ('title', 'active', 'partner_website')
    

admin.site.register(Partner, PartnerAdmin)