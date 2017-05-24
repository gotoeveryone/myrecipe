"""
WSGI config for recipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application

ENVFILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
dotenv.read_dotenv(ENVFILE)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipe.settings")

application = get_wsgi_application()
