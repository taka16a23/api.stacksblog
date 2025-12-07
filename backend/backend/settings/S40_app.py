#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S04_app --

"""
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auth_logger',
    'rest_framework',
    'drf_spectacular',
    'django_summernote',
    'django_filters',
    'corsheaders',
    'base',
    'db_stamp',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # SessionMiddlewareの後かつCommonMiddlewareの前に記載すること
    # sessionとURL prefixesを利用するため
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ),
    'DEFAULT_FILTER_BACKENDS': (
      'django_filters.rest_framework.DjangoFilterBackend',
      'rest_framework.filters.OrderingFilter',
      'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

WSGI_APPLICATION = 'backend.wsgi.application'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S40_app.py ends here
