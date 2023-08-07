#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S21_path --

"""
import os
from pathlib import Path


# project base directory path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# translation file paths
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# base templates paths
TEMPLATE_PATHS = [os.path.join(BASE_DIR, 'templates')]

# project data paths
DATA_DIR = '/var/www/'

# static file path
STATIC_ROOT = os.path.join(DATA_DIR, '/var/www/static')

# media root path
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# 21_path.py ends here
