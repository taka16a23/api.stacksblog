#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tel_input -- tel input

"""
from django.forms.widgets import Input


class TelInput(Input):
    input_type = 'tel'
    template_name = 'django/forms/widgets/text.html'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tel_input.py ends here
