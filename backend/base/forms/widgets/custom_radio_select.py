#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""custom_radio_select -- Custom radio select button

"""
from django.forms import RadioSelect


class CustomRadioSelect(RadioSelect):
    """CustomRadioSelect

    CustomRadioSelect is a RadioSelect.
    Responsibility:
    """
    option_template_name = 'forms/widgets/custom_radio_option.html'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# custom_radio_select.py ends here
