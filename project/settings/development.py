import sys

from common import *
from . import secret

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = # fill it ('multiad.dev.djangostars.com',)

SECRET_KEY = secret('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secret('DB_NAME'),
        'USER': secret('DB_USER'),
        'PASSWORD': secret('DB_PASS'),
    }
}

#REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ()
