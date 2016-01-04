import re
import time

from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import resolve

from .models import *
from .conf.settings import CLOCKGUARD_REDIRECT_URL

class BlockControlMiddleware(object):
	def process_request(self, request):
		current_resolver = resolve(request.path_info)

		if ClockGuardModel.objects.filter(page_name=current_resolver.url_name).exists():
			if int(time.time()) > int(ClockGuardModel.objects.filter(page_name=current_resolver.url_name)[0].page_start_time):
				return request
			else:
				return redirect(CLOCKGUARD_REDIRECT_URL)