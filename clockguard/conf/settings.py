from django.conf import settings

CLOCKGUARD_REDIRECT_URL = '/'
if hasattr(settings, 'CLOCKGUARD_REDIRECT_URL'):
	CLOCKGUARD_REDIRECT_URL = getattr(settings, 'CLOCKGUARD_REDIRECT_URL')

CLOCKGUARD_ROOT_URL = getattr(settings, 'ROOT_URLCONF')
if hasattr(settings, 'CLOCKGUARD_ROOT_URL'):
	CLOCKGUARD_ROOT_URL = getattr(settings, 'CLOCKGUARD_ROOT_URL')
