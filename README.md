django-redmine-auth-backend
===========================

A Django authentication backend for use with the Redmine.

## Install

Using pip:

    pip install -e git+https://github.com/daniel-yavorovich/django-redmine-auth-backend.git

Otherwise, download the code any way you like and do:

    python setup.py install

## Configure Django for using Redmine auth backend

Please define AUTHENTICATION_BACKENDS
and REDMINE_URL in Django settings file:

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'redmine_auth.backends.RedditBackend',
    )

    REDMINE_URL = 'https://redmine.example.com'


