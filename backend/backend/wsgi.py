"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys
import site

site.addsitedir('/var/www/webapp/venv/lib/python3.8/site-packages')

if not '/var/www/webapp/backend' in sys.path:
    sys.path.append('/var/www/webapp/backend')
if not '/var/www/backend/backend' in sys.path:
    sys.path.append('/var/www/backend/backend')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
