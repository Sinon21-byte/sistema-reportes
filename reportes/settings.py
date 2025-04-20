from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'tu-secret-key'
DEBUG = False

ALLOWED_HOSTS = [
    'sistema-reportes-021i.onrender.com',  # tu dominio de Render
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    # WhiteNoise debe ir antes de cualquier middleware que sirva archivos estáticos
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

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

# ——— Base de datos SQLite interna ———
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ——— Archivos estáticos ———
STATIC_URL = '/static/'

# Le decimos a Django dónde están tus assets de desarrollo
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'core' / 'static',
]

# Carpeta donde collectstatic volcará los archivos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Almacenamiento optimizado de WhiteNoise (compressed + cache busting)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ——— Media (uploads temporales) ———
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
