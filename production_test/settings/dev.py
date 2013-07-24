from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

try:
	from .local import *
except ImportError:
	pass
