import re

from django.http import HttpResponseRedirect
from clockguard.models import *

class BlockControlMiddleware(object):
	def process_request(self, request):