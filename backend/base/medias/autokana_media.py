#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""autokana_media -- autokana media

"""
from django import forms
from .jquery_media import JQUERY_MEDIA


AUTO_KANA_MEDIA = forms.Media(
    css={},
    js=[
        'js/jquery.autoKana.js',
        'admin/js/jquery.init.js',
    ]
)
AUTO_KANA_MEDIA += JQUERY_MEDIA



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# autokana_media.py ends here
