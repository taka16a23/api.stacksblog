#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_admin_media -- base admin model form media

"""
from django import forms
from .jquery_media import JQUERY_MEDIA


BASE_ADMIN_MEDIA = forms.Media(
    css={'screen': [
        'css/tooltip.css',
        'css/custom_admin.css',
        'css/custom_listview_admin.css',
    ],},
    js=[
        'admin/js/jquery.init.js',
        'js/filter_collapse.js',
    ]
)
BASE_ADMIN_MEDIA = JQUERY_MEDIA + BASE_ADMIN_MEDIA



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_admin_media.py ends here
