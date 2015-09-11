"""
Django settings for tedxostrava project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%y5eth^%_rk31anmt57)4s%qr2b@jz1y3j^79ld)1%g))_jsuo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'events',
    'speakers',
    'partners',
    'news',
    'tedx',
    'cloudinary',
    'mobile_settings',
    'rest_framework_swagger',
    'django_crontab',
    'sorl.thumbnail',
    'push_notifications',
)

SITE_ID = 1

PUSH_NOTIFICATIONS_SETTINGS = {
        "GCM_API_KEY": "<your api key>",
        "APNS_CERTIFICATE": "/path/to/your/certificate.pem",
}


CRONJOBS = [
    ('*/1 * * * *', 'tedxostrava.cron.my_scheduled_job')
]

USE_I18N = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

cloudinary.config( 
  cloud_name = "hydqixw1j", 
  api_key = "199655958195283", 
  api_secret = "fgx9gXSnw1mvQ3we1jsB-vxBJwA" 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'tedxostrava.urls'

TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

SUIT_CONFIG = {
    'MENU': (

        'sites',
        'speakers',
        'events',
        'news',
        'partners',
        'tedx',

        

        {'app': 'auth', 'models': ('user', 'group')},

    ),
    'MENU_EXCLUDE': ('home'),
    'MENU_OPEN_FIRST_CHILD': True,
    
    
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'tedxostrava.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
from django.utils.translation import ugettext
ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('cs', ugettext('Czech')),
)



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

#STATICFILES_DIRS = (
 #   os.path.join(BASE_DIR, "static", "static_dirs"),
#)

#STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dc5p35khseegrh',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'oywtzcfdeedpke',
        'PASSWORD': 'UU9PnAJi1VqQyvscIa2pqvmk2F',
        'HOST': 'ec2-54-83-18-87.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()




# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
#STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'tedxostrava.utils.jwt_response_payload_handler',

      'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=933300),
}
