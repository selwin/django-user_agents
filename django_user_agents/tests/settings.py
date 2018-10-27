import django
from os import path


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = ['django_user_agents']

if django.VERSION >= (1, 10):
    MIDDLEWARE = [
        'django_user_agents.middleware.UserAgentMiddleware',
    ]
else:
    MIDDLEWARE_CLASSES = [
        'django_user_agents.middleware.UserAgentMiddleware',
    ]

ROOT_URLCONF = 'django_user_agents.tests.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60,
        'LOCATION': 'default-location',
    },
    'test': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60,
        'LOCATION': 'test-location',
    },
}

if django.VERSION >= (1, 8):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                path.join(path.dirname(__file__), "templates"),
            ],
        },
    ]
else:
    TEMPLATE_DIRS = (
        path.join(path.dirname(__file__), "templates"),
    )

SECRET_KEY = 'foobarbaz'
