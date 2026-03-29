from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from startpage import views
from startpage.views import AdminLoginView, StudentLoginView, StudentSignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startpage.urls')),
    # Choose whether to log in as admin or student
    path('login/', views.choose_login, name='login'),
    path('login/admin/', AdminLoginView.as_view(), name='login_admin'),
    path('login/student/', StudentLoginView.as_view(), name='login_student'),
    path('signup/student/', StudentSignupView.as_view(), name='signup_student'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]
