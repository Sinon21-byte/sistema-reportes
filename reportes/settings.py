from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-test-key'
DEBUG = True
ALLOWED_HOSTS = [
    'sistema-reportes-021i.onrender.com',
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = []

# --- Si no lo tenías, asegúrate de esto: ---
ROOT_URLCONF = 'reportes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

WSGI_APPLICATION = 'reportes.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# ——— Añadido para servir las imágenes subidas sin base de datos ———
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Evita la advertencia de clave automática 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

