#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_stamp_admin_mixin --

"""
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.safestring import mark_safe


class StampAdminMixin(object):
    """StampAdminMixin

    StampAdminMixin is a object.
    Responsibility:
    """
    def created(self, obj):
        result = ''
        if obj.created_by is not None:
            result += str(obj.created_by)
        if obj.created_by is None:
            result += '-'
        result += '<br>'
        result += obj.created_at.strftime("%Y/%m/%d %H:%M:%S")
        return mark_safe(result)

    created.short_description = _('created')

    def modified(self, obj):
        result = ''
        if obj.modified_by is not None:
            result += str(obj.modified_by)
        if obj.created_by is None:
            result += '-'
        result += '<br>'
        result += obj.modified_at.strftime("%Y/%m/%d %H:%M:%S")
        return mark_safe(result)

    modified.short_description = _('modified')

    def save_model(self, request, obj, form, change):
        obj.set_user(request.user)
        return super(StampAdminMixin, self).save_model(request, obj, form, change)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_stamp_admin_mixin.py ends here
