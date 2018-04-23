from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_wJQGnHfgKP7A5TwD4x93baZu')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_YgCqwaPXGPgMoi9YaZEPBIbi')

SITE_URL = 'https://pet-sail.herokuapp.com'
ALLOWED_HOSTS.append('pet-sail.herokuapp.com')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
