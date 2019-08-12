# Setting file for python Raspberry PI server
# Change only the needed setting for the PI


import os
from .settings_local import *

SECRET_KEY = os.getenv("SECRET_KEY_ENV")

ALLOWED_HOSTS = [
    '127.0.0.1',
    '142.122.50.151',
    '192.168.2.37',
    'nicolasgagne.freeddns.org',
]

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE_ENV"),
        'NAME': os.path.join(BASE_DIR, os.getenv("DATABASE_NAME_ENV")),
    }
}