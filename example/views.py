from django.shortcuts import render_to_response
from django.template import RequestContext

from clockguard.decorators import *
from datetime import time

@everyday_time_control(start_time=time(8, 0, 0), end_time=time(9, 0, 0))
def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
