"""
ASGI config for citrus project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citrus.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Add other protocols later.
}) 
