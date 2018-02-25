"""
WSGI config for recipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import join, dirname

from dotenv import read_dotenv
from django.core.wsgi import get_wsgi_application

# Get environment variable
read_dotenv(join(dirname(__file__), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")

application = get_wsgi_application()
