from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')  # Use environment variable for production
# DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
DEBUG = True

ALLOWED_HOSTS = ['*']  # Adjust for production with specific domains

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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

ROOT_URLCONF = 'seagull.urls'

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

WSGI_APPLICATION = 'seagull.wsgi.application'

# Database configuration removed since you don't use a database
DATABASES = {}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration
# STATICFILES_DIRS = [BASE_DIR / 'static',  BASE_DIR / "app/static"]
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build")  # Ensure this is correct

# STATICFILES_DIRS = [BASE_DIR / 'seagull' / 'static',]

# Directories where static files are located
STATICFILES_DIRS = [
    BASE_DIR / "app/static",
]

# Path to store collected static files (for production)
STATIC_ROOT = BASE_DIR / 'staticfiles_build'
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.OverwriteStorage"
# URL for static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",  # For project-wide static files
#     BASE_DIR / "app/static",  # For app-specific static files
# ]
# STATIC_ROOT = BASE_DIR / 'staticfiles_build'  # Directory for `collectstatic` to use in production

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'seagulltechhr@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Load password from environment
DEFAULT_FROM_EMAIL = 'seagulltechhr@gmail.com'
ADMIN_EMAIL = 'seagulltechhr@gmail.com'