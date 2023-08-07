#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sample_product_local --

"""
####from .S30_security import *


DEBUG = False

SECRET_KEY = '{secretkey}'

####SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY


# MySQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "webapp",
        "USER": "webapp",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

# Email
EMAIL_HOST_PASSWORD = ''


if __name__ == '__main__':
    import sys
    from pathlib import Path
    this_file_path = Path(__file__)
    directory_path = this_file_path.parent
    local_file_name = 'S90_local.py'
    local_file_path = directory_path.joinpath(local_file_name)
    if local_file_path.exists() == True:
        print('{} already exists.Remove it.'.format(local_file_name))
        sys.exit(-1)
    from django.core.management.utils import get_random_secret_key
    secret_key = get_random_secret_key()
    file_contents = this_file_path.read_text()
    file_contents = file_contents.replace('{secretkey}', secret_key, 1)
    file_contents = file_contents.replace('####', '')
    local_file_path.write_text(file_contents)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sample_product_local.py ends here
