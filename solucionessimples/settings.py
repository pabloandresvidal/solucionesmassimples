"""
Django settings for solucionessimples project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf import settings
from os.path import abspath, basename, dirname, join, normpath
import os
########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Site name.
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)

SITE_ID = 1
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# -*- coding: utf-8 -*-

gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-(##u^aql!cq&s^@za*av$(4^bryi4y=52zx5=tpv&wv@^9p08'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = '/home/pablovidal/webapps/static'

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files.
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
    #normpath(join(DJANGO_ROOT, 'templates')),
    os.path.join(PROJECT_PATH, "templates"),
)


CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

ALLOWED_HOSTS = [
    'www.solucionesmassimples.com', # Allow domain and subdomains
    'solucionesmassimples.com.', # Also allow FQDN and subdomains
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.messages',
    'core',
    'south',
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
    'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    'djangocms_text_ckeditor',

    #'django-filer',
    #'cmsplugin_filery',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'solucionessimples.urls'

WSGI_APPLICATION = 'solucionessimples.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'

LANGUAGES = [
    ('es-co', 'Spanish'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login'



EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'gerencia_solucionesmassimples'
EMAIL_HOST_PASSWORD = 'TechDesign2014'
DEFAULT_FROM_EMAIL = 'gerencia@solucionesmassimples.com'
SERVER_EMAIL = 'gerencia@solucionesmassimples.com'
