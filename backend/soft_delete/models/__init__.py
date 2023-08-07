#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.forms import widgets
from django.contrib.admin import options

from soft_delete.models.datetimeflag_field import DateTimeFlagField
from soft_delete import forms


__all__ = [ 'DateTimeFlagField', ]

options.FORMFIELD_FOR_DBFIELD_DEFAULTS[DateTimeFlagField] = {
    'form_class': forms.DateTimeFlagField,
    'widget': widgets.CheckboxInput}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
