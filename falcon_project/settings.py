
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "replace-this-in-env")
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Render adds a hostname like: myapp.onrender.com
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'falcon_project.main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # REQUIRED ON RENDER
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'falcon_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'falcon_project.wsgi.application'

# ---------- STATIC FILES ----------
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "falcon_project" / "main" / "static"
]

# Location where Render will collect static files
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise production static file handler
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
