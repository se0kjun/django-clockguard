import re
import time

from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import resolve

from clockguard.models import *

class BlockControlMiddleware(object):
	def process_request(self, request):
		if hasattr(settings, 'CLOCKGUARD_REDIRECT_URL'):
			redirect_url = getattr(settings, 'CLOCKGUARD_REDIRECT_URL')
		current_resolver = resolve(request.path_info)

		if ClockGuardModel.objects.filter(page_name=current_resolver.url_name).exists():
			if int(time.time()) > int(ClockGuardModel.objects.filter(page_name=current_resolver.url_name)[0].page_start_time):
				# event
			else:
				# redirect