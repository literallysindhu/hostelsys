import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

print("Available users:")
for u in User.objects.all():
    print(f" - {u.username} (is_staff: {u.is_staff}, role: {getattr(u, 'role', 'N/A')})")

u1 = authenticate(username='testadmin', password='testadmin123')
u2 = authenticate(username='csstudent', password='student123')

print("Admin auth testadmin/testadmin123:", "SUCCESS" if u1 else "FAILED")
print("Student auth csstudent/student123:", "SUCCESS" if u2 else "FAILED")
