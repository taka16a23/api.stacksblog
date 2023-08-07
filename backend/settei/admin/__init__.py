#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin

from settei.models import SetteiModel
from settei.admin.settei_model_admin import SetteiModelAdmin


__all__ = [
    'SetteiModelAdmin',
]

admin.site.register(SetteiModel, SetteiModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
