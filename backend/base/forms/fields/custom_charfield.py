#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""custom_charfield -- custom charfield

"""
from django.forms import CharField


class CustomCharField(CharField):
    """CustomCharField

    CustomCharField is a CharField.
    Responsibility:
    """

    def __init__(self, **kwargs):
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        self.max_length = kwargs.get('max_length', '')
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
            t_result['maxlength'] = self.max_length
        if self.placeholder:
            t_result['placeholder'] = self.placeholder
        return t_result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# custom_charfield.py ends here
