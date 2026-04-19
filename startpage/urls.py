from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('students/', views.students, name='students'),
    path('complaints/', views.complaints, name='complaints'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('outpasses/', views.outpasses, name='outpasses'),
    path('mess-menu/', views.mess_menu, name='mess_menu'),
    path('snacks/', views.snacks, name='snacks'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('student-fees/', views.student_fees, name='student_fees'),
]
