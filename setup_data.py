import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model
from startpage.models import Hostel, Room, StudentProfile, Complaint

User = get_user_model()

# Create test admin
if not User.objects.filter(username='testadmin').exists():
    admin = User.objects.create_superuser('testadmin', 'testadmin@example.com', 'testadmin123')
    admin.role = User.Role.ADMIN
    admin.department = 'CSE'
    admin.save()
    print("Created testadmin user")

# Create test student
if not User.objects.filter(username='sr1070@srmist.edu.in').exists():
    student_user = User.objects.create_user(
        username='sr1070@srmist.edu.in',
        email='sr1070@srmist.edu.in',
        password='elsaandnokk',
        first_name='Test',
        last_name='Student',
        role=User.Role.STUDENT,
        register_number='SR1070',
        department='CSE'
    )
    print("Created test student user")

    # Create dummy hostel & room
    hostel, _ = Hostel.objects.get_or_create(name='Main Boys Hostel', block='A', total_floors=3, warden_name='Mr. Warden')
    room, _ = Room.objects.get_or_create(hostel=hostel, room_number='A101', capacity=2, room_type=Room.RoomType.NON_AC)
    
    # Create profile
    StudentProfile.objects.create(
        user=student_user,
        department='CSE',
        year='2nd Year',
        room=room,
        guardian_phone='1234567890',
        address='123 Main St'
    )
    print("Created student profile, hostel, and room")
    
    # Create sample complaint
    Complaint.objects.create(
        student=student_user,
        room=room,
        category='Maintenance',
        description='Fan is not working properly.',
        status=Complaint.Status.PENDING
    )
    print("Created sample complaint")

print("Setup complete")
