from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class DashboardAccessTests(TestCase):
    def setUp(self):
        self.username_staff = 'sind'
        self.password = 'password123'
        self.staff_user = User.objects.create_user(self.username_staff, 'sind@example.com', self.password)
        self.staff_user.is_staff = True
        self.staff_user.save()

        self.username_student = 'student'
        self.student_user = User.objects.create_user(self.username_student, 'student@example.com', self.password)

    def test_staff_sees_admin_dashboard(self):
        logged_in = self.client.login(username=self.username_staff, password=self.password)
        self.assertTrue(logged_in)
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Admin Dashboard')
        # counts should be present (0 by default in test DB)
        self.assertContains(resp, 'Rooms')
        self.assertContains(resp, 'Students')
        self.assertContains(resp, 'Complaints')

    def test_non_staff_sees_dashboard(self):
        logged_in = self.client.login(username=self.username_student, password=self.password)
        self.assertTrue(logged_in)
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Student Dashboard')


class LoginFlowTests(TestCase):
    def setUp(self):
        self.staff_username = 'adminuser'
        self.password = 'pass1234'
        self.staff = User.objects.create_user(self.staff_username, 'admin@example.com', self.password)
        self.staff.is_staff = True
        self.staff.save()

        self.student_username = 'stud'
        self.student = User.objects.create_user(self.student_username, 'stud@example.com', self.password)

    def test_choose_login_shows_options(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, reverse('login_admin'))
        self.assertContains(resp, reverse('login_student'))

    def test_admin_login_allows_staff(self):
        resp = self.client.post(reverse('login_admin'), {'username': self.staff_username, 'password': self.password}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Admin Dashboard')

    def test_admin_login_rejects_nonstaff(self):
        resp = self.client.post(reverse('login_admin'), {'username': self.student_username, 'password': self.password})
        # form invalid should return 200 and show error
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'This account is not an admin')

    def test_student_login_allows_student(self):
        resp = self.client.post(reverse('login_student'), {'username': self.student_username, 'password': self.password}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Student Dashboard')

    def test_student_login_rejects_admin(self):
        resp = self.client.post(reverse('login_student'), {'username': self.staff_username, 'password': self.password})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Please use the admin login for admin accounts.')

    def test_logout_works_with_post(self):
        # login as student then logout via POST
        logged_in = self.client.login(username=self.student_username, password=self.password)
        self.assertTrue(logged_in)
        resp = self.client.post(reverse('logout'), follow=True)
        self.assertEqual(resp.status_code, 200)
        # After logout, we should be redirected to the choose-login page
        self.assertContains(resp, 'I Am..')
