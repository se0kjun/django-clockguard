from django import forms
from django.conf import settings

from clockguard.models import *

class InsertClockGuardForm(forms.Form):
	page_url = forms.ChoiceField(required=True, widget=forms.Select())
	page_block_start_time = forms.IntegerField(required=False)
	page_block_end_time = forms.IntegerField(required=False)

	def __init__(self, *args, **kwargs):
		super(InsertClockGuardForm, self).__init__(*args, **kwargs)
		self.fields['page_url'].choices = self._get_url_list()
	
	def _get_url_list(self):
		_url_list = []
		if hasattr(settings, 'CLOCKGUARD_ROOT_URL'):
			urlconf = __import__(getattr(settings, 'CLOCKGUARD_ROOT_URL'), {}, {}, [''])
		elif hasattr(settings, 'ROOT_URLCONF'):
			urlconf = __import__(getattr(settings, 'ROOT_URLCONF'), {}, {}, [''])
		else:
			return None

		for url in urlconf.urlpatterns:
			if hasattr(url, '_urlconf_module'):
				_url_list.extend(_get_url_recursive(url))
			else:
				_url_list.append(url._regex)

		return _url_list


	def _get_url_recursive(self, module):
		url_module = module._urlconf_module
		url_list = []
		for pat in url_module.urlpatterns:
			if hasattr(pat, '_urlconf_module'):
				url_list.extend(self._get_url_recursive(pat))
			else:
				url_list.append(pat._regex)
				continue

		return url_list

