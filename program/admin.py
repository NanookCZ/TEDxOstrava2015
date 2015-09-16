from django.contrib import admin
from .models import Section, Schedule, SlotKind, Slot, Presentation

admin.site.register(Section)
admin.site.register(Schedule)
admin.site.register(SlotKind)
admin.site.register(Slot)
admin.site.register(Presentation)



