#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""custom_url_field -- custom url field

"""
from django.forms import URLField


class CustomURLField(URLField):
    """CustomURLField

    CustomURLField is a URLField.
    Responsibility:
    """

    def __init__(self, **kwargs):
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        self.placeholder = kwargs.pop('placeholder', '')
        super().__init__(**kwargs)

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        t_result = {'class': 'vTextField', }
        if self.max_length:
            t_result['max_length'] = self.max_length
        if self.placeholder:
            t_result['placeholder'] = self.placeholder
        return t_result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# custom_url_field.py ends here
