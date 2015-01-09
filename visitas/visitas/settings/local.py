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

# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/index"
# Redirect when login is not correct.
LOGIN_URL = '/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')