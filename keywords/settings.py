import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^#&71w(ku)zf+$66**_8269_8s)qbq^10h&kukr*5eoijvcdxw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'word'
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'keywords.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'word/templates/word')],
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

WSGI_APPLICATION = 'keywords.wsgi.application'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, 'word/static/word'),
]

# Search links
CATALOG_SUFFIX = '&tab=Everything&search_scope=MyInst_and_CI&vid=01UTAU_INST:SEARCH&lang=en&offset=0'
CATALOG_LINK = 'https://search.lib.utexas.edu/discovery/search?query=any,contains,'
ACADEMIC_SEARCH_LINK = 'http://web.a.ebscohost.com/ehost/resultsadvanced?vid=1&bdata=JmRiPWE5aCZ0eXBlPTEmc2l0ZT1laG9zdC1saXZl&bquery='
JSTOR_LINK = 'https://www.jstor.org/action/doBasicSearch?Query='