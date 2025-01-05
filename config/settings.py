from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lt^(d$!8t-z5omzz^kodp-ygdrx3v3jpctiy2d_#)3k56$*opx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Defined Apps
    'preferences.apps.PreferencesConfig',
    'accounts.apps.AccountsConfig',
    'base.apps.BaseConfig',
    'pages.apps.PagesConfig',

    # Third Party Apps
    'phonenumber_field',
    'bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Bilingual settings
LANGUAGES = [
    ('en', _('English')),
    ('fa', _('Persian')),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = 'media/'

if DEBUG:
    STATIC_ROOT = BASE_DIR / 'static/'
    MEDIA_ROOT = BASE_DIR / 'media/'

    STATICFILES_DIRS = [
        'base/static',
    ]
else:
    STATIC_ROOT = ''
    MEDIA_ROOT = ''

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vinzei.co@gmail.com'
EMAIL_HOST_PASSWORD = 'gfbqakcgodcatucy'

# Auto Logout Variable
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=30),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}
if LANGUAGE_CODE == 'fa-ir':
    AUTO_LOGOUT['MESSAGE'] = 'بخاطر غیر فعال بودن، زمان استفاده از حساب کاربری تمام شده است.\
     لطفا برای ادامه دوباره وارد شوید.'
else:
    AUTO_LOGOUT['MESSAGE'] = 'The session has expired. Please login again to continue.'
