from django.http import HttpResponse
from .models import Room, StudentProfile, Complaint, Outpass, MessMenu
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentLoginForm, StudentSignupForm, AdminLoginForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection, models

def home(request):
    return render(request, 'home.html')

@login_required
def rooms(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('dashboard')
    rooms_list = Room.objects.select_related('hostel').all()
    return render(request, 'rooms.html', {'rooms_list': rooms_list})

@login_required
def students(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('dashboard')
        
    if request.method == 'POST' and 'update_student' in request.POST:
        profile_id = request.POST.get('profile_id')
        new_room_id = request.POST.get('room_id')
        new_year = request.POST.get('year')
        if profile_id:
            try:
                profile = StudentProfile.objects.get(id=profile_id)
                if new_room_id:
                    profile.room_id = new_room_id if new_room_id != 'none' else None
                if new_year:
                    profile.year = new_year
                profile.save()
                messages.success(request, f"Updated {profile.user.username}'s profile successfully.")
            except StudentProfile.DoesNotExist:
                messages.error(request, "Student not found.")
        return redirect('students')

    students_list = StudentProfile.objects.select_related('user', 'room', 'room__hostel').order_by('-created_at')
    
    # Department Filtering for Admins
    if request.user.department:
        students_list = students_list.filter(department=request.user.department)

    available_rooms = Room.objects.all()
    return render(request, 'students.html', {'students_list': students_list, 'available_rooms': available_rooms})

@login_required
def complaints(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('dashboard')
        
    if request.method == 'POST' and 'update_status' in request.POST:
        complaint_id = request.POST.get('complaint_id')
        new_status = request.POST.get('status')
        admin_note = request.POST.get('admin_note')
        if complaint_id:
            try:
                c = Complaint.objects.get(id=complaint_id)
                if new_status:
                    c.status = new_status
                if admin_note is not None:
                    c.admin_note = admin_note
                c.save()
                messages.success(request, f'Complaint updated successfully!')
            except Complaint.DoesNotExist:
                messages.error(request, 'Complaint not found!')
            return redirect('complaints')

    complaints_list = Complaint.objects.select_related('student', 'room').order_by('-created_at')
    
    # Department Filtering for Admins
    if request.user.department:
        complaints_list = complaints_list.filter(student__student_profile__department=request.user.department)
    
    # Generate simple AI recommendations if missing
    for c in complaints_list:
        if not c.ai_recommendation:
            rec = "Assign relevant staff to handle this."
            cat = c.category.lower()
            if "maintenance" in cat:
                rec = "Schedule maintenance team review within 24hrs."
            elif "electrical" in cat:
                rec = "Dispatch campus electrician immediately. Check circuit breakers."
            elif "plumbing" in cat:
                rec = "Call plumbing contractor. Instruct student to locate water valve."
            elif "cleaning" in cat:
                rec = "Add to priority list for housekeeping tomorrow morning."
            
            c.ai_recommendation = rec
            c.save()
    
    context = {
        'complaints_list': complaints_list,
    }
    return render(request, 'complaints.html', context)

@login_required
def outpasses(request):
    is_admin = request.user.is_staff or request.user.is_superuser
    
    if request.method == 'POST':
        if is_admin and 'update_status' in request.POST:
            outpass_id = request.POST.get('outpass_id')
            new_status = request.POST.get('status')
            admin_note = request.POST.get('admin_note')
            if outpass_id:
                try:
                    op = Outpass.objects.get(id=outpass_id)
                    if new_status:
                        op.status = new_status
                    if admin_note is not None:
                        op.admin_note = admin_note
                    op.save()
                    messages.success(request, 'Outpass updated successfully.')
                except Outpass.DoesNotExist:
                    messages.error(request, 'Outpass not found.')
        elif not is_admin and 'apply_outpass' in request.POST:
            destination = request.POST.get('destination')
            reason = request.POST.get('reason')
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            if destination and reason and from_date and to_date:
                Outpass.objects.create(
                    student=request.user,
                    destination=destination,
                    reason=reason,
                    from_date=from_date,
                    to_date=to_date
                )
                messages.success(request, 'Outpass submitted successfully. Waiting for admin approval.')
        
        return redirect('outpasses')

    if is_admin:
        outpasses_list = Outpass.objects.select_related('student', 'student__student_profile').order_by('-created_at')
        if request.user.department:
            outpasses_list = outpasses_list.filter(student__student_profile__department=request.user.department)
    else:
        outpasses_list = request.user.outpasses.all()
        
    context = {
        'outpasses_list': outpasses_list,
        'is_admin': is_admin,
    }
    return render(request, 'outpasses.html', context)

@login_required
def mess_menu(request):
    menus = MessMenu.objects.all()
    
    # Optional sorting logic to ensure logical day order
    day_order = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}
    menus = sorted(menus, key=lambda m: day_order.get(m.day, 8))
    
    context = {
        'menus': menus,
        'is_admin': request.user.is_staff or request.user.is_superuser,
    }
    return render(request, 'mess_menu.html', context)

def choose_login(request):
    """Landing page that asks whether the user is an admin or a student."""
    return render(request, 'choose_login.html')


class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = AdminLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Only allow staff/superuser accounts on the admin login page
        user = form.get_user()
        if user.is_staff or user.is_superuser:
            selected_dept = form.cleaned_data.get('department')
            if user.department and selected_dept and user.department != selected_dept:
                form.add_error(None, f'Access Denied: You are a {user.department} admin, restricting you from the {selected_dept} terminal.')
                return self.form_invalid(form)
            elif not user.department and selected_dept:
                # Assign selected department choice to admin's profile/field if none
                user.department = selected_dept
                user.save(update_fields=['department'])
            return super().form_valid(form)
        form.add_error(None, 'This account is not an admin. Please use the student login.')
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class StudentLoginView(LoginView):
    template_name = 'student_login.html'
    authentication_form = StudentLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        # Prevent staff users from logging in via the student login page
        if user.is_staff or user.is_superuser:
            form.add_error(None, 'Please use the admin login for admin accounts.')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class StudentSignupView(FormView):
    template_name = 'student_signup.html'
    form_class = StudentSignupForm
    success_url = reverse_lazy('login_student')

    def form_valid(self, form):
        User = get_user_model()
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['full_name'],
            register_number=form.cleaned_data['register_number'],
            department=form.cleaned_data['department'],
            role=User.Role.STUDENT
        )
        # Create profile
        StudentProfile.objects.create(
            user=user,
            department=form.cleaned_data['department'],
            year='1st Year' # Default
        )
        
        messages.success(self.request, 'Account created successfully! Please login.')
        return super().form_valid(form)


@login_required
def profile(request):
    """Student profile page"""
    student_profile = None
    try:
        student_profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        pass
    
    context = {
        'student_profile': student_profile,
    }
    return render(request, 'profile.html', context)


@login_required
def dashboard(request):
    # Show a dedicated admin dashboard for staff users
    if request.user.is_staff or request.user.is_superuser:
        sql_result = None
        sql_error = None
        
        if request.method == 'POST' and 'execute_sql' in request.POST:
            raw_sql = request.POST.get('raw_sql')
            if raw_sql:
                try:
                    with connection.cursor() as cursor:
                        # Disable foreign key constraints temporarily for testing/review deletions
                        if connection.vendor == 'sqlite':
                            cursor.execute('PRAGMA foreign_keys = OFF;')
                            
                        # If multiple statements, executescript is needed for sqlite
                        if ';' in raw_sql and not raw_sql.strip().lower().startswith("select"):
                            cursor.executescript(raw_sql)
                            sql_result = f"Command script executed successfully!"
                        else:
                            cursor.execute(raw_sql)
                            # Fetch results if it's a SELECT query, otherwise just commit and show row count
                            if raw_sql.strip().lower().startswith("select"):
                                columns = [col[0] for col in cursor.description]
                                rows = cursor.fetchall()
                                sql_result = {'columns': columns, 'rows': rows}
                            else:
                                sql_result = f"Command executed successfully! Rows affected: {cursor.rowcount}"
                                
                        # Re-enable foreign key constraints
                        if connection.vendor == 'sqlite':
                            cursor.execute('PRAGMA foreign_keys = ON;')
                except Exception as e:
                    sql_error = str(e)
                    # Ensure FKs are turned back on even if there's an error
                    if connection.vendor == 'sqlite':
                        with connection.cursor() as cursor:
                            cursor.execute('PRAGMA foreign_keys = ON;')
                    
        room_count = Room.objects.count()
        
        # Filtering dashboard data by department
        q_students = StudentProfile.objects.all()
        q_complaints = Complaint.objects.all()
        q_outpasses = Outpass.objects.all()
        
        if request.user.department:
            q_students = q_students.filter(department=request.user.department)
            q_complaints = q_complaints.filter(student__student_profile__department=request.user.department)
            q_outpasses = q_outpasses.filter(student__student_profile__department=request.user.department)
            
        student_count = q_students.count()
        complaint_count = q_complaints.count()
        outpass_count = q_outpasses.filter(status='PENDING').count()
        recent_complaints = q_complaints.select_related('student').order_by('-created_at')[:5]
        
        User = get_user_model()
        admin_users_base = User.objects.filter(models.Q(is_staff=True) | models.Q(role=User.Role.ADMIN))
        if request.user.department:
            admin_users_base = admin_users_base.filter(department=request.user.department)
        admin_users = admin_users_base.distinct().order_by('-date_joined')
        
        student_users = User.objects.filter(role=User.Role.STUDENT, student_profile__in=q_students).select_related('student_profile', 'student_profile__room').order_by('-date_joined')
        
        # Get all database tables to show in the console reference
        db_tables = connection.introspection.table_names()
        
        context = {
            'room_count': room_count,
            'student_count': student_count,
            'complaint_count': complaint_count,
            'outpass_count': outpass_count,
            'recent_complaints': recent_complaints,
            'sql_result': sql_result,
            'sql_error': sql_error,
            'admin_users': admin_users,
            'student_users': student_users,
            'db_tables': db_tables,
        }
        return render(request, 'admin_dashboard.html', context)
    
    # Student dashboard
    student_profile = None
    room = None
    hostel = None
    my_complaints = []
    latest_outpass = None
    todays_menu = None
    try:
        student_profile = request.user.student_profile
        room = student_profile.room
        if room:
            hostel = room.hostel
        my_complaints = request.user.complaints.all()[:3]
        latest_outpass = request.user.outpasses.first()
        
        import datetime
        today_code = datetime.datetime.now().strftime('%a').upper()
        # Mapping for SUN -> SUN, but some locales might differ, so hardcode a small map if needed
        # Our model uses MON, TUE, WED, THU, FRI, SAT, SUN
        todays_menu = MessMenu.objects.filter(day=today_code).first()
    except StudentProfile.DoesNotExist:
        pass
        
    if request.method == 'POST' and 'submit_complaint' in request.POST:
        category = request.POST.get('category')
        description = request.POST.get('description')
        if category and description:
            Complaint.objects.create(
                student=request.user,
                room=room,
                category=category,
                description=description
            )
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('dashboard')
    
    context = {
        'student_profile': student_profile,
        'room': room,
        'hostel': hostel,
        'my_complaints': my_complaints,
        'latest_outpass': latest_outpass,
        'todays_menu': todays_menu,
    }
    return render(request, 'dashboard.html', context)