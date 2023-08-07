#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin
from django.contrib.auth.models import Permission
from account.models.account_model import AccountUser
from account.admin.account_user_admin import AccountUserAdmin
from account.admin.permission_admin import PermissionAdmin

__all__ = [
    'AccountUserAdmin',
    'PermissionAdmin',
]

admin.site.register(AccountUser, AccountUserAdmin)
admin.site.register(Permission, PermissionAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
