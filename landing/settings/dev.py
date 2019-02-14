from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
