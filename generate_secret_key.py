""" SECRET_KEY生成用 """
from django.core.management import utils

print(utils.get_random_secret_key())
