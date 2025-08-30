import os
from django.core.wsgi import get_wsgi_application

# Django settings modulini belgilaymiz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grammar_api.settings')

# WSGI application obyektini yaratamiz
application = get_wsgi_application()
