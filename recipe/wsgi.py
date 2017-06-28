"""
WSGI config for recipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from os.path import join, dirname

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

DOTENV_PATH = join(dirname(__file__), '../.env')
load_dotenv(DOTENV_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")

application = get_wsgi_application()
