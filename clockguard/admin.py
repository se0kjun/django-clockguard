from django.contrib import admin

from .models import ClockGuardModel

class ClockGuardAdmin(admin.ModelAdmin):
	pass

admin.site.register(ClockGuardModel, ClockGuardAdmin)
