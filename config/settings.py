from __future__ import unicode_literals

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'development_db',
        'USER': 'development_user',
        'OPTIONS': {
            'sql_mode': 'STRICT_ALL_TABLES',
        },
    },
}

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.expanduser('~/media/')
MEDIA_URL = '/media/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'events',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SECRET_KEY = 'development_secret_key'
X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'config.urls'

SITE_ID = 1

STATIC_URL = '/static/'
