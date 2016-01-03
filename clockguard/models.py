from __future__ import unicode_literals

from django.db import models

class ClockGuardModel(models.Model):
	page_url = models.TextField(unique=True)
	page_name = models.TextField(default=None)
	page_start_time = models.IntegerField()
	page_end_time = models.IntegerField()

	def __unicode__(self):
		return self.page_url

