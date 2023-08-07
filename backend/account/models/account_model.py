#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""account_model -- define login account model

"""
import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm
from django.contrib.auth.models import PermissionsMixin
from base.models.base_stamp_mixin import BaseStampMixin
from soft_delete.models.softdelete_mixin import SoftDeleteMixin
from django.utils.translation import gettext_lazy as _

from account.models.account_manager import AccountManager


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('images/users', filename)


class AccountUser(AbstractBaseUser, PermissionsMixin,
                  BaseStampMixin, SoftDeleteMixin):
    """AccountUser

    | Physical Name | type     | size | NN | PK | FK         | IDX | default | description                                |
    | account_id    | bigint   |      |    | Y  |            |     |         |                                            |
    | email         | nvarchar |  245 | Y  |    |            |     |         | メールアドレスは一意なので、ログインに利用 |
    | username      | nvarchar |  150 | Y  |    |            |     | ''      |                                            |
    | password      | nvarchar |  128 | Y  |    |            |     |         | SHA256 hash                                |
    | is_superuser  | bool     |      | Y  |    |            |     | false   |                                            |
    | last_login    | datetime |      |    |    |            |     |         |                                            |
    | is_active     | bool     |    1 | Y  |    |            |     | 1       | ユーザー認証許可フラグ                         |
    | description   | nvarchar | 2000 | Y  |    |            |     | ''      |                                            |
    | avatar        | nvarchar |      |    |    |            |     | NULL    |                                            |
    | created_at    | datetime |      |    |    |            |     | now()   |                                            |
    | created_by    | int      |      |    |    | account_id |     | Null    |                                            |
    | modified_at   | datetime |      |    |    |            |     | now()   |                                            |
    | modified_by   | int      |      |    |    | account_id |     | Null    |                                            |
    | deleted_at    | datetime |      |    |    |            |     | Null    | 削除なら日時、否ならNULL                   |
    """
    account_id = models.BigAutoField(_('ID'), primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        unique=False,
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        _('Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    # system use
    is_staff = models.BooleanField(
        default=True,
    )
    description = models.TextField(
        _('Description'),
        default='',
        null=False,
        blank=True,
        help_text=_('Description'),
    )
    avatar = models.ImageField(
        upload_to=get_file_path,
        null=True,
        blank=True,
    )

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = 'account'
        swappable = 'AUTH_USER_MODEL'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# account_model.py ends here
