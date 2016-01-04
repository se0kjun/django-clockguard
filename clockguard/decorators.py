from django.http import HttpResponseRedirect
import time
from functools import wraps

from .conf.settings import CLOCKGUARD_REDIRECT_URL
from .manager import *
from .exception import RedirectCycleException

def everyday_time_control(start_time, end_time, redirect_url=CLOCKGUARD_REDIRECT_URL, user_pass=True):
    def _wrapper(func):
        @wraps(func)
        def _wrap(request, *args, **kwargs):
            if request.path == redirect_url:
                raise RedirectCycleException("redirect cycle")

            manager = EveryDayManager(start_time, end_time)
            if manager.check():
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(redirect_url)
        return _wrap
    return _wrapper

def everyweek_time_control(start_time, end_time, day, redirect_url=CLOCKGUARD_REDIRECT_URL, user_pass=True):
    def _wrapper(func):
        def _wrap(*args, **kwargs):
            if request.path == redirect_url:
                raise RedirectCycleException("redirect cycle")

            manager = EveryWeekManager(start_time, end_time, day)
            if manager.check():
                return func(*args, **kwargs)
            else:
                return HttpResponseRedirect(redirect_url)
        return _wrap
    return _wrapper

def everymonth_time_control(start_time, end_time, date, redirect_url=CLOCKGUARD_REDIRECT_URL, user_pass=True):
    def _wrapper(func):
        def _wrap(*args, **kwargs):
            if request.path == redirect_url:
                raise RedirectCycleException("redirect cycle")

            manager = EveryMonthManager(start_time, end_time)
            if manager.check():
                return func(*args, **kwargs)
            else:
                return HttpResponseRedirect(redirect_url)
        return _wrap
    return _wrapper

def everyyear_time_control(start_time, end_time, date, redirect_url=CLOCKGUARD_REDIRECT_URL, user_pass=True):
    def _wrapper(func):
        def _wrap(*args, **kwargs):
            if request.path == redirect_url:
                raise RedirectCycleException("redirect cycle")
                
            manager = EveryYearManager(start_time, end_time)
            if manager.check():
                return func(*args, **kwargs)
            else:
                return HttpResponseRedirect(redirect_url)
        return _wrap
    return _wrapper