from .base import *

ALLOWED_HOSTS = ['www.ilanalab.com', 'ilanalab.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ilana',
        'USER': 'ubuntu',
        'PASSWORD': 'ilanalab',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = '/var/www/ilana/static/'
MEDIA_ROOT = '/var/www/ilana/media/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
