"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv() # This is actually loading our .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DJANGO_DEBUG']

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1', '192.168.1.153']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom
    'generator.apps.GeneratorConfig',
    'custom_auth.apps.CustomAuthConfig',
    # 3rd Party
    'custom_pwa',  # Technically this is custom but its copied
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ]
# MEDIA_URL = '/images/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
AUTH_USER_MODEL = 'custom_auth.CustomUser'

AUTHENTICATION_BACKENDS = [
    'custom_auth.utils.CustomModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/auth/login/'
LOGOUT_REDIRECT_URL = ''

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_SANDBOX_MODE_IN_DEBUG = os.environ['SENDGRID_SANDBOX_MODE_IN_DEBUG']
SENDGRID_ECHO_TO_STDOUT = os.environ['SENDGRID_ECHO_TO_STDOUT']
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
DEFAULT_FROM_EMAIL = os.environ['DJANGO_DEFAULT_FROM_EMAIL']
CONTACT_EMAIL = os.environ['DJANGO_CONTACT_EMAIL']

# === PWA ===
PWA_APP_NAME = 'maths_question_generator'
PWA_APP_DESCRIPTION = "Maths Question Generator PWA"
PWA_APP_THEME_COLOR = '#333333'
PWA_APP_BACKGROUND_COLOR = '#EEEEEE'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': 'static/images/site-logo-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/images/site-logo-160x160.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/images/site-logo-160x160.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_DEBUG_MODE = os.environ['PWA_APP_DEBUG_MODE']  # This does not work for some reason?

# Stripe
DEV_STRIPE_PK_KEY = os.environ['DEV_STRIPE_PK_KEY']  # Public Key (development)
DEV_STRIPE_SK_KEY = os.environ['DEV_STRIPE_SK_KEY']  # Secret Key (development)
DEV_STRIPE_WEBHOOK_SK = os.environ['DEV_STRIPE_WEBHOOK_SK']