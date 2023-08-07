#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""jquery_media -- Jquery media

"""
from django import forms
from django.conf import settings

JQUERY_MEDIA = forms.Media(
    css={},
    js=[
        'admin/js/vendor/jquery/jquery{}.js'
        .format('' if settings.DEBUG else '.min'),
        'admin/js/jquery.init.js',
    ]
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# jquery_media.py ends here
