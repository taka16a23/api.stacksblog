#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""datetimeflag_field -- datetimeflag field

"""
from django.db.models import DateTimeField
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import widgets

from soft_delete import forms


class DateTimeFlagField(DateTimeField):
    """DateTimeFlagField

    DateTimeFlagField is a DateTimeField.
    Responsibility:
    """
    default_error_messages = {
        'invalid': _('Value %(value)r is not a valid check.'),
        'null': _('This field cannot be null.'),
        'blank': _('This field cannot be blank.'),
    }
    description = _("Deleted flag")

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': forms.DateTimeFlagField,
            **kwargs,
        })



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# datetimeflag_field.py ends here
