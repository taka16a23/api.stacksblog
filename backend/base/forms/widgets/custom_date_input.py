#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""custom_date_input -- custom date input

"""
from django.forms.widgets import DateInput


class CustomDateInput(DateInput):
    input_type = 'date'
    template_name = 'django/forms/widgets/date.html'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# custom_date_input.py ends here
