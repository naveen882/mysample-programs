"""
Django settings for hpro project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1ed@3o(p+1__4l674%hz#0f6+ro##&+#p=8k%+^5y3cv%(bq9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	 'app1',
	 'app2',
	 'app3',
#    'djcelery',		
#	 'django_extensions', #for generating relationship graphs
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
	 'middleware.crossdomainxhr.XsSharing',
)

ROOT_URLCONF = 'hpro.urls'

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

WSGI_APPLICATION = 'hpro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASE_ROUTERS = ['manager.router.DatabaseAppsRouter']
#DATABASE_APPS_MAPPING = {'app1': 'db1', 
#                         'app2':'db2'}
from manager import app2db 
DATABASE_APPS_MAPPING = app2db.mapping
print DATABASE_APPS_MAPPING
                        
#DATABASES = {
#    'default': {
#    },
#	 'db1': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'hpro1',
#        'USER': 'root',
#        'PASSWORD': 'hp123',
#		  'PORT': '3306'
#	 },
#	 'db2': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'hpro2',
#        'USER': 'root',
#        'PASSWORD': 'hp123',
#		  'PORT': '3306'
#	 }
#}

DATABASES = {
    'default': {
    },
	 'db1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'appserver_core',
        'USER': 'appserver',
        'PASSWORD': 'data',
		  'HOST': '10.0.3.7',
		  'PORT': '3306'
	 },
	 'db2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'appserver_coreone',
        'USER': 'appserver',
        'PASSWORD': 'data',
		  'HOST': '10.0.3.7',
		  'PORT': '3306'
	 }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/") #added mabnually by me

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/hpro.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'app1': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

#CELERY SETTINGS
#BROKER_URL = "django://hpro:hpro@localhost:5672/<RABBIT_VHOST>"
#CELERY_RESULT_BACKEND = "database"

# choose the setting that matches your database of choice
#CELERY_RESULT_DBURI = "mysql://root:hp123@localhost/celery_db"
#CELERY_RESULT_DBURI = "postgresql://<DB_USER>:<DB_PASSWORD>@localhost/<DB_NAME>"
#INSTALLED_APPS += ('kombu.transport.django', )

# put these two lines at the very bottom of the settings file
#import djcelery
#djcelery.setup_loader()

