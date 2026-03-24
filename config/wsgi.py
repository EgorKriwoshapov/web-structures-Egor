"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# WhiteNoise by default serves only STATIC files.
# Explicitly add MEDIA directory to serve user uploads at /media/.
application = WhiteNoise(application)
application.add_files(str(settings.MEDIA_ROOT), prefix=settings.MEDIA_URL.lstrip('/'))