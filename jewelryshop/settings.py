

from pathlib import Path

import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-3%y3laftm62q0zaj+s7#p-xqq9(&#q+)s8)p-&#&bz*0$!xu$0'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jewelryshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_preprocessors.store_menu',
                'store.context_preprocessors.cart_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'jewelryshop.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Vercel SQLite Workaround
# Vercel filesystem is read-only, so we copy the DB to /tmp (writable)
if os.environ.get('VERCEL') or 'VERCEL' in os.environ:
    try:
        import shutil
        DB_FILE = os.path.join(BASE_DIR, 'db.sqlite3')
        TMP_DB_FILE = '/tmp/db.sqlite3'
        
        # Check if we can write to /tmp
        if os.access('/tmp', os.W_OK):
            # Only copy if source exists
            if os.path.exists(DB_FILE):
                # If tmp does not exist or size is different, copy
                # If it exists, we might want to keep it to persist data across requests in same lambda
                # But for safety, let's copy if it doesn't exist
                if not os.path.exists(TMP_DB_FILE):
                     shutil.copyfile(DB_FILE, TMP_DB_FILE)
                
                DATABASES['default']['NAME'] = TMP_DB_FILE
    except Exception as e:
        print(f"Error copying DB to /tmp: {e}")




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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'jewelryshop/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
