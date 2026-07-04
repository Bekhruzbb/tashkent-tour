import os
import sys
from django.core.wsgi import get_wsgi_application

# Добавляем корневую директорию в пути, чтобы Python видел папку project
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()

app = application
