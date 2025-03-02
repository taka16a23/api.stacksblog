#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S30_security --

"""
from datetime import timedelta

# カスタムユーザーモデル
# AUTH_USER_MODEL = 'account.AccountUser'

# SECURITY WARNING: keep the secret key used in production secret!
# generate
# from django.core.management.utils import get_random_secret_key
# get_random_secret_key()
SECRET_KEY = ''

ALLOWED_HOSTS = ['*', ]

#CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://blog.taka16a23.com',
    'https://blog.taka16a23.com',
    'http://blogapi.taka16a23.com',
    'http://blogapi.taka16a23.com:8080',
    'https://blogapi.taka16a23.com',
    'http://blog.taka16a23.com.s3-website-ap-northeast-1.amazonaws.com',
    'https://main.d3marf7vppdnlc.amplifyapp.com',
    'https://test-blog.taka16a23.com',
    'https://dev-blog.taka16a23.com/',
]

CORS_ORIGIN_REGEX_WHITELIST = [
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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

# JWT 関連
JWT_AUTH = {
}

SIMPLE_JWT = {
}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S30_security.py ends here
