import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from startpage.models import Fee
from django.contrib.auth import get_user_model

User = get_user_model()

# Create a Pending Fee for all Student users if they don't have one
students = User.objects.filter(role=User.Role.STUDENT)
for student in students:
    if not Fee.objects.filter(student=student).exists():
        Fee.objects.create(
            student=student,
            amount=45000.00,
            semester='Even Semester 2026',
            payment_status=Fee.PaymentStatus.PENDING
        )
        print(f"Created pending fee for {student.username}")

print("Fee creation script finished.")
