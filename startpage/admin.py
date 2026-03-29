from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Hostel, Room, StudentProfile, Complaint, Fee, Outpass, MessMenu

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'register_number', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'register_number', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'register_number', 'phone')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(StudentProfile)
admin.site.register(Complaint)
admin.site.register(Fee)
admin.site.register(Outpass)
admin.site.register(MessMenu)
