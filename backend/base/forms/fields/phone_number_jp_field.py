#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""phone_number_jp_field -- phone number jp form field

"""
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy as _

from .custom_charfield import CustomCharField
from base.forms.widgets.tel_input import TelInput

from utils.patterns import PatternFactory


class PhoneNumberJPField(CustomCharField):
    """PhoneNumberJPField

    PhoneNumberJPField is a CustomCharField.
    Responsibility:
    """
    widget = TelInput
    default_validators = [
        RegexValidator(PatternFactory.PHONE_NUMBER_JP,
                       message=_('Incorrect phone number.'))]

    def __init__(self, **kwargs):
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        kwargs.setdefault('max_length', 21)
        self.pattern = kwargs.pop('pattern', '[0-9-]+')
        super().__init__(**kwargs)

    def widget_attrs(self, widget):
        """
        Given a Widget instance (*not* a Widget class), return a dictionary of
        any HTML attributes that should be added to the Widget, based on this
        Field.
        """
        import inspect, logging
        logging.getLogger('django.debug').debug('Called {0.__class__.__name__}.{1}'.format(self, inspect.currentframe().f_code.co_name))
        t_attrs = super(PhoneNumberJPField, self).widget_attrs(widget)
        if self.pattern != '':
            t_attrs.setdefault('pattern', self.pattern)
        return t_attrs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# phone_number_jp_field.py ends here
