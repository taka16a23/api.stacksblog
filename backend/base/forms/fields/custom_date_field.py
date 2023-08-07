#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""custom_date_field -- custom date input field

"""
from django.forms import DateField
from base.forms.widgets.custom_date_input import CustomDateInput


class CustomDateField(DateField):
    """CustomDateField

    CustomDateField is a DateField.
    Responsibility:
    """
    widget = CustomDateInput

    def __init__(self, **kwargs):
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        self.step = kwargs.pop('step', '')
        self.min = kwargs.pop('min', '')
        self.max = kwargs.pop('max', '')
        super().__init__(**kwargs)

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        t_result = {}
        if self.step:
            t_result['step'] = self.step
        if self.min:
            t_result['min'] = self.min
        if self.max:
            t_result['max'] = self.max
        return t_result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# custom_date_field.py ends here
