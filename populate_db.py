import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth import get_user_model
from startpage.models import Hostel, Room, StudentProfile, Complaint, Fee, Outpass, MessMenu

User = get_user_model()

def populate():
    print("Populating initial data...")
    
    # 1. MessMenu
    menus = [
        ('MON', 'Dosa, Chutney', 'Rice, Dal, Cabbage', 'Samosa, Tea', 'Roti, Paneer Butter Masala'),
        ('TUE', 'Idli, Sambar', 'Rice, Rasam, Potato', 'Vada, Coffee', 'Roti, Chicken Curry or Gobi Manchurian'),
        ('WED', 'Poha, Jalebi', 'Rice, Dal Makhani', 'Puff, Juice', 'Roti, Mixed Veg'),
        ('THU', 'Upma, Bhujia', 'Veg Biryani, Raita', 'Cake, Milk', 'Roti, Egg Curry or Dal Fry'),
        ('FRI', 'Aloo Paratha, Curd', 'Rice, Sambar, Beans', 'Maggi, Tea', 'Roti, Fish Curry or Chana Masala'),
        ('SAT', 'Puri, Sabzi', 'Khichdi, Papad', 'Bhel Puri', 'Roti, Rajma'),
        ('SUN', 'Chole Bhature', 'Chicken Biryani or Veg Pulao', 'Biscuit, Coffee', 'Roti, Aloo Gobi'),
    ]
    for day, bf, lu, sn, di in menus:
        MessMenu.objects.get_or_create(day=day, defaults={
            'breakfast': bf, 'lunch': lu, 'snacks': sn, 'dinner': di
        })
        
    # 2. Hostels
    hostel1, _ = Hostel.objects.get_or_create(
        name='Main Boys Hostel', defaults={'block': 'A', 'total_floors': 3, 'warden_name': 'Mr. Sharma'}
    )
    hostel2, _ = Hostel.objects.get_or_create(
        name='Main Girls Hostel', defaults={'block': 'B', 'total_floors': 2, 'warden_name': 'Mrs. Gupta'}
    )

    # 3. Rooms
    room1, _ = Room.objects.get_or_create(
        hostel=hostel1, room_number='A101', defaults={'capacity': 2, 'room_type': Room.RoomType.NON_AC, 'current_occupancy': 1}
    )
    room2, _ = Room.objects.get_or_create(
        hostel=hostel2, room_number='B101', defaults={'capacity': 3, 'room_type': Room.RoomType.AC, 'current_occupancy': 2}
    )
    room3, _ = Room.objects.get_or_create(
        hostel=hostel1, room_number='A102', defaults={'capacity': 2, 'room_type': Room.RoomType.AC, 'current_occupancy': 0}
    )

    # 4. Users & Profiles
    if not User.objects.filter(username='alice@srmist.edu.in').exists():
        alice = User.objects.create_user(
            username='alice@srmist.edu.in', email='alice@srmist.edu.in', password='password123',
            first_name='Alice', last_name='Smith', role=User.Role.STUDENT, register_number='SR1071', department='ECE'
        )
        StudentProfile.objects.create(
            user=alice, department='ECE', year='1st Year', room=room2, 
            guardian_phone='9876543210', address='123 Maple Street'
        )
        # Fee for Alice
        Fee.objects.create(
            student=alice, amount=25000.00, semester='Spring 2026', 
            payment_status=Fee.PaymentStatus.PAID, paid_on=date(2026, 1, 15)
        )
        # Outpass for Alice
        Outpass.objects.create(
            student=alice, destination='Local Guardian House', reason='Weekend Discharged',
            from_date=date(2026, 4, 10), to_date=date(2026, 4, 12), status=Outpass.Status.APPROVED
        )
        print("Created student Alice.")

    if not User.objects.filter(username='bob@srmist.edu.in').exists():
        bob = User.objects.create_user(
            username='bob@srmist.edu.in', email='bob@srmist.edu.in', password='password123',
            first_name='Bob', last_name='Johnson', role=User.Role.STUDENT, register_number='SR1072', department='MECH'
        )
        StudentProfile.objects.create(
            user=bob, department='MECH', year='3rd Year', room=room1, 
            guardian_phone='5551234567', address='456 Oak Avenue'
        )
        # Fee for Bob
        Fee.objects.create(
            student=bob, amount=20000.00, semester='Spring 2026', 
            payment_status=Fee.PaymentStatus.PENDING
        )
        # Complaint from Bob
        Complaint.objects.create(
            student=bob, room=room1, category='Electrical', 
            description='Tubelight is flickering.', status=Complaint.Status.PENDING
        )
        print("Created student Bob.")

    print("Database populated successfully with extra tables.")

if __name__ == '__main__':
    populate()
