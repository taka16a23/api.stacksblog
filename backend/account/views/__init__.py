#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from account.views.account_user_viewset import AccountUserViewSet
from account.views.account_user_simple_viewset import AccountUserSimpleViewSet
from account.views.login_user_viewset import LoginUserView
from account.views.permission_viewset import PermissionViewSet
from account.views.group_viewset import GroupViewSet
from account.views.password_change_viewset import PasswordChangeViewset

__all__ = [
    'AccountUserViewSet',
    'AccountUserSimpleViewSet',
    'LoginUserView',
    'PermissionViewSet',
    'GroupViewSet',
    'PasswordChangeViewset',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
