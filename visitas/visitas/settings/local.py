from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'visitasdb',
        'USER': 'dgar',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')