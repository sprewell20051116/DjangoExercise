from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qdekc@z$t&x(!npwz3_a+i24-h4@00&%0zyskokv*=o-ur-@%*'
DEBUG = True
TEMPLATE_DEBUG = True
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}