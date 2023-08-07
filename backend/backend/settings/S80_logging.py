#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""S80_logging --

"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        # 'file': {
            # 'level': 'INFO',
            # 'class': 'logging.FileHandler',
            # 'filename': '/var/log/webapp.log',
        # },
    },
    # 'root': {
        # 'handlers': ['console', 'file'],
        # 'level': 'DEBUG',
    # },
}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# S80_logging.py ends here
