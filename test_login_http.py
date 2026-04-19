import requests

session = requests.Session()

# Get CSRF token
response = session.get('http://127.0.0.1:8000/login/')
csrf_token = session.cookies['csrftoken']

# Try logging in as admin
payload = {
    'csrfmiddlewaretoken': csrf_token,
    'username': 'testadmin',
    'password': 'testadmin123',
    'role': 'admin',
    'department': 'CSE',
}
headers = {'Referer': 'http://127.0.0.1:8000/login/'}
post_response = session.post('http://127.0.0.1:8000/login/admin/', data=payload, headers=headers, allow_redirects=False)

print("Admin Login status code:", post_response.status_code)
if post_response.status_code == 302:
    print("Redirects to:", post_response.headers.get('Location'))
else:
    print("FAILED admin login. Response text snippet:", post_response.text[:500])

# Try logging in as student
session2 = requests.Session()
response2 = session2.get('http://127.0.0.1:8000/login/')
csrf_token2 = session2.cookies['csrftoken']

payload2 = {
    'csrfmiddlewaretoken': csrf_token2,
    'username': 'csstudent',
    'password': 'student123',
    'role': 'student',
    # Even though hidden, JS might still send department depending on form serialization
    'department': 'CSE',
}
post_response2 = session2.post('http://127.0.0.1:8000/login/student/', data=payload2, headers=headers, allow_redirects=False)

print("\nStudent Login status code:", post_response2.status_code)
if post_response2.status_code == 302:
    print("Redirects to:", post_response2.headers.get('Location'))
else:
    print("FAILED student login. Response text snippet:", post_response2.text[:500])
