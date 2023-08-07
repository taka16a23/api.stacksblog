#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""datetimeflag_field -- datetime flag field

"""
import inspect
import logging
import datetime

from django import forms
from django.forms.utils import from_current_timezone


class DateTimeFlagField(forms.DateTimeField):
    """DateTimeFlagField

    DateTimeFlagField is a forms.DateTimeField.
    Responsibility:
    """
    widget = forms.CheckboxInput

    def has_changed(self, initial, data):
        logging.getLogger('kintai').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        if self.disabled:
            return False
        if initial is not None and data is not None:
            return False
        # Sometimes data or initial may be a string equivalent of a boolean
        # so we should run it through to_python first to get a boolean value
        init_py = self.to_python(initial)
        data_py = self.to_python(data)
        return init_py != data_py

    def to_python(self, value):
        """Convert bool to datetime object if value is True.

        to_python(value)

        @Arguments:
        - `value`: bool or datetime

        @Return: convert to datetime now if boolean

        @Error:
        """
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        if isinstance(value, (datetime.datetime, )):
            return value
        result = None
        if value == True:
            result = datetime.datetime.now()
            return from_current_timezone(result)
        return result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# datetimeflag_field.py ends here
