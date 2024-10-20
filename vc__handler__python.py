import os
from django.core.asgi import get_asgi_application

# Set the default settings module for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'land.settings')

# Get the ASGI application
application = get_asgi_application()
