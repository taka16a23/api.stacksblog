#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account_manager -- define account manager

"""
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_account(self, username, email, password, is_staff=False, is_superuser=False, **kwargs):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_active=True,
            created_at=now,
            **kwargs,
        )
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')
        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            created_at=now,
        )
        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        now = timezone.now()
        request_data = {
            'username': username,
            'email': email,
            'password': password,
            'created_at': now,
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account_manager.py ends here
