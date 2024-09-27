# setup_script.py

import os
from django.conf import settings
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Configure Django settings
settings.configure()

# Initialize Django
django.setup()

# Now you can access Django's models and other functionalities
