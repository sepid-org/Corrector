from datetime import timedelta
from corrector.settings.base import *

DEBUG = get_environment_var('DEBUG', 'False') == 'True'

SECRET_KEY = get_environment_var(
    'SECRET_KEY', '*z!3aidedw32xh&1ew(^&5dgd17(ynnmk=s*mo=v2l_(4t_ff(')

ALLOWED_HOSTS = get_environment_var('ALLOWED_HOSTS', '*').split(',')

SERVICE_DOMAIN = 'https://corrector.sepid.org/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, get_environment_var(
    'STATIC_ROOT_FILE_NAME', 'staticfiles'))

LOG_LEVEL = get_environment_var('LOG_LEVEL', 'INFO')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)-8s [%(module)s:%(funcName)s:%(lineno)d]: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'logging/debug.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'django': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'corrector': {
            'handlers': ['file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}

TESTING = False

SWAGGER_URL = f'{SERVICE_DOMAIN}api/'

CSRF_TRUSTED_ORIGINS = get_environment_var('CSRF_TRUSTED_ORIGINS').split(',')
