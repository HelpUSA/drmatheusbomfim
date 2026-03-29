# File: config/settings.py
# Purpose:
# Django settings for the Dr. Matheus Bomfim website.
# This project is intentionally simple and focused on a small institutional website.
# Updated for production deployment (Vercel compatibility + host fix).

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECURITY =================

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-change-me-before-production')

# DEBUG control via env
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

# Allow local, Vercel, and custom production hosts, with environment override support.
ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS',
    '127.0.0.1,localhost,.vercel.app,drmatheusbomfim.helpusbr.com'
).split(',')

# ================= APPS =================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

# ================= MIDDLEWARE =================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Important for static files in production.
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================= URL / TEMPLATES =================

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'website' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# ================= DATABASE =================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ================= AUTH =================

AUTH_PASSWORD_VALIDATORS = []

# ================= INTERNATIONALIZATION =================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# ================= STATIC FILES =================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'website' / 'static'
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Django 5.x recommended storage configuration.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ================= DEFAULT =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'