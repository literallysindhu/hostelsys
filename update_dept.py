import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model
from startpage.models import StudentProfile

User = get_user_model()
User.objects.all().update(department='CSE')
StudentProfile.objects.all().update(department='CSE')
print("All users and profiles updated to CSE department.")
