#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""char_number_field -- char as nuber field

"""
from .custom_charfield import CustomCharField


class CharNumberField(CustomCharField):
    """CharNumberField

    CharNumberField is a CustomCharField.
    Responsibility:
    """

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        t_result = super(CharNumberField, self).widget_attrs(widget)
        t_result.setdefault('pattern', '[0-9]+')
        return t_result



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# char_number_field.py ends here
