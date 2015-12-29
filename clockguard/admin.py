from django.contrib import admin

from clockguard.models import *

class ClockGuardAdmin(admin.ModelAdmin):
	pass

admin.site.register(ClockGuardModel, ClockGuardAdmin)
