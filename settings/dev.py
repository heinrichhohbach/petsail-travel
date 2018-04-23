from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_wJQGnHfgKP7A5TwD4x93baZu')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_YgCqwaPXGPgMoi9YaZEPBIbi')
