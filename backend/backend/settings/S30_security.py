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

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://blog.taka16a23.com',
    'https://blog.taka16a23.com',
    'http://blogapi.taka16a23.com',
    'http://blogapi.taka16a23.com:8080',
    'https://blogapi.taka16a23.com',
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
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.views.jwt_response_payload_handler',
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 'JWT_PAYLOAD_HANDLER': 'auth.views.jwt_response_payload_handler.jwt_response_payload_handler',
    # 'JWT_ALGORITHM': 'HS256',
    # 'JWT_ALLOW_REFRESH': True,
}

SIMPLE_JWT = {
    # Do not change security reason
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    # Change here for login life time
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # 'ROTATE_REFRESH_TOKENS': True,
    # 'BLACKLIST_AFTER_ROTATION': True,
    # 'UPDATE_LAST_LOGIN': True,

    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,

    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_FIELD': 'account_id',
    # 'USER_ID_CLAIM': 'user_id',

    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',

    # 'JTI_CLAIM': 'jti',

    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S30_security.py ends here
