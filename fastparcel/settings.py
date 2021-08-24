"""
Django settings for fastparcel project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b3xoe-@_&50f5a9v0t=8!e84g=miygz4ylo@z!lfisodc@sk-='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'bootstrap4',
    'core.apps.CoreConfig',
    'channels'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'core.middleware.ProfileMiddleware'
]

ROOT_URLCONF = 'fastparcel.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'fastparcel.context_processors.export_vars',
            ],
        },
    },
]

WSGI_APPLICATION = 'fastparcel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/sign-in'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = "544745680203048"
SOCIAL_AUTH_FACEBOOK_SECRET = "f93bc07943543fb03d83860a90807eac"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['GMAIL_ACCOUNT']
EMAIL_HOST_PASSWORD = os.environ['GMAIL_PASS']
DEFAULT_FROM_EMAIL = 'Fast Parcel <no-reply@fastparcel.localhost>'

FIREBASE_ADMIN_CREDENTIAL = os.path.join(
    BASE_DIR, "fastparcel-df78b-firebase-adminsdk-oi4ak-4f0c4257ec.json")

STRIPE_API_PUBLIC_KEY = "pk_test_51JOJ2VBw903sikgMxkGWLWtSmsMMx4S1VtuCdSQuBNPwYoz9uXP8B5qmeNuzIjfBtO6CfPwp6xaBAq74N5fFaXGI00HsQNv4jr"
STRIPE_API_SECRET_KEY = "sk_test_51JOJ2VBw903sikgMIIpvxEZiFqaZmt82oApohvribgKJoBfL1CxWhaUQvtWeY2RhEqkMGGrcF0ciUJWdWhMkc0TO00t3PvwT1b"

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

PAYPAL_MODE = "sandbox"
PAYPAL_CLIENT_ID = os.environ['PAYPAL_CLIENT_ID']
PAYPAL_CLIENT_SECRET = os.environ['PAYPAL_CLIENT_SECRET']

NGROK_URL = os.environ['NGROK_URL']

ASGI_APPLICATION = "fastparcel.asgi.application"
