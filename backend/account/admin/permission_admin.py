#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""permission_admin -- permission admin

"""
from django.contrib import admin


class PermissionAdmin(admin.ModelAdmin):
    """PermissionAdmin

    PermissionAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = (
        'id',
        'name',
        'content_type_id',
        'codename',
    )
    list_display_links = (
        'name',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# permission_admin.py ends here
