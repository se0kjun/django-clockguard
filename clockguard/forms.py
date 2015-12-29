from django import forms

from clockguard.models import *

class InsertClockGuardForm(forms.Form):
	page_url = forms.ChoiceField(required=True, widget=forms.Select())

	def __init__(self, *args, **kwargs):
		super(InsertClockGuardForm, self).__init__(*args, **kwargs)

