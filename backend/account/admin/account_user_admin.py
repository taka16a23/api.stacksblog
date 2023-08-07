#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""AccountUserAdmin -- Account User Admin

"""
from django.contrib import admin


class AccountUserAdmin(admin.ModelAdmin):
    """AccountUserAdmin

    AccountUserAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'account_id',
        'email',
        'username',
        'is_active',
        'is_superuser',
        'description',
    )
    list_editable = (
        'is_active',
    )
    list_filter = (
        'is_active',
        'is_superuser',
    )
    ordering = (
        'account_id',
    )
    filter_horizontal = (
        'user_permissions',
        'groups',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# AccountUserAdmin.py ends here
