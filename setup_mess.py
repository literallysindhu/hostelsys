import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from startpage.models import MessMenu

def add_menu(day, b, l, s, d):
    m, _ = MessMenu.objects.get_or_create(day=day)
    m.breakfast = b
    m.lunch = l
    m.snacks = s
    m.dinner = d
    m.save()

add_menu('MON', 'Dosa, Chutney, Sambhar', 'Rice, Dal, Mixed Veg Curry', 'Samosa, Tea', 'Chapati, Paneer Sabzi, Rice')
add_menu('TUE', 'Idli, Vada, Sambhar', 'Rice, Rajma, Aloo Gobi', 'Puff, Coffee', 'Poori, Chana Masala, Rice')
add_menu('WED', 'Poha, Jalebi', 'Rice, Chicken Curry / Paneer Butter Masala', 'Biscuits, Tea', 'Chapati, Dal Tadka, Rice')
add_menu('THU', 'Aloo Paratha, Curd', 'Veg Biryani, Raita', 'Bonda, Tea', 'Chapati, Mix Veg, Rice')
add_menu('FRI', 'Upma, Kesari Bath', 'Rice, Sambhar, Rasam, Fish Fry/Gobi 65', 'Cake, Coffee', 'Chapati, Egg Curry/Dal, Rice')
add_menu('SAT', 'Masala Dosa, Chutney', 'Rice, Dal Makhani', 'Pav Bhaji', 'Fried Rice, Manchurian')
add_menu('SUN', 'Chole Bhature', 'Chicken Biryani / Veg Pulao', 'Pakora, Tea', 'Chapati, Dal, Rice')

print("Mess menu setup complete.")
