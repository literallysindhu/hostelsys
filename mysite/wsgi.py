"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Vercel ephemeral SQLite hack for portfolio deployments
original_db = BASE_DIR / 'db.sqlite3'
tmp_db = Path('/tmp/db.sqlite3')

if os.environ.get('VERCEL') == '1' and original_db.exists():
    if not tmp_db.exists():
        shutil.copy2(original_db, tmp_db)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

app = application
