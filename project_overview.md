# HostelSys - Database Management Project Overview

## 1. Project Introduction
**HostelSys** is a comprehensive Hostel Database Management System built using the Django framework (Python). The main objective of this application is to digitalize and streamline the administrative operations of a university or college hostel. 

The system implements role-based access control, catering to two primary types of users:
* **Students**: Can view their room, manage their profile, apply for outpasses, raise maintenance complaints, and view their fee structures and mess menus.
* **Administrators (Admins/Wardens)**: Can manage hostel infrastructure (rooms, capacities), approve/reject outpasses, process complaints, and oversee student records and fee payments.

---

## 2. Technology Stack
* **Backend Framework**: Django (Python)
* **Database**: SQLite3 (Default for Django, suitable for development and lightweight local management)
* **Frontend/UI**: HTML/CSS templates (incorporating a customized, fully responsive web design and dashboard)
* **Data Reporting**: `pandas` and `openpyxl` used for data manipulation and exporting SQLite data into formats such as Excel (`.xlsx`) and structured text schemas.

---

## 3. Core Features
### 3.1. User Management & Authentication
* The system utilizes a custom `User` model, extending Django's built-in `AbstractUser`. 
* Uses **Role-Based Access Control (RBAC)** to restrict actions depending on whether the logged-in user is a "STUDENT" or an "ADMIN".
* Collects detailed university-specific attributes such as `register_number` and `department` upon registration.

### 3.2. Accommodation Management (Hostels & Rooms)
* Admins can create and manage multiple hostel buildings (e.g., Boys Hostel, Girls Hostel) defined by distinct blocks, floors, and warden assignments.
* Within each hostel, individual rooms are tracked. 
* Rooms enforce capacity limits automatically. The system raises validation errors if occupied beds exceed the specified room capacity. 

### 3.3. Complaint / Maintenance Desk
* A digital ticketing system that allows students to report issues (e.g., Electrical, Plumbing, Maintenance) bound directly to their respective rooms.
* Admins can update the state of the complaint (Pending -> In Progress -> Resolved) and attach administrative notes.
* Contains a unique field for **AI Recommendations** aimed at suggesting quick fixes or routing tasks efficiently.

### 3.4. Leave & Outpass Management
* Replaces paper-based permission slips. Students request leaves by defining their destination, reason, and duration.
* Wardens/Admins review pending outpasses and update their status to "Approved" or "Rejected" along with specific administrative feedback.

### 3.5. Financial Tracking & Fee Portal
* Manages the financial relationship between the hosteller and the hostel management. 
* Tracks varying fee amounts, corresponding semesters, and updates payment statuses (Pending to Paid). 
* Includes a fully functional simulated payment gateway that dynamically synchronizes with the `Fee` model via secure AJAX `fetch()` requests. Features a realistic PIN verification flow and instant receipt generation without page reloads.
* The Admin Dashboard instantly aggregates `Total Collected` and `Total Pending` sums globally, reflecting successful student transactions instantly.

### 3.6. Mess Menu
* An interactive database schedule detailing the food menu (Breakfast, Lunch, Snacks, Dinner) for each day of the week.

### 3.7. Smart Vending Machine
* Students can reserve daily snacks with built-in restrictions limiting users to 3 reservations per day.
* Enforces an automated 24-hour lockout mechanism via session tracking for heavy consumers to prevent hoarding.
* Generates random 6-digit one-time-passwords (OTPs) upon reservation for verified claimability at physically connected hardware nodes.

### 3.8. Internal Data Exporting & Reporting Tools
* A robust scripting backend dedicated to data analysis and extraction.
* Custom scripts heavily utilize Pandas and Python's built-in sqlite3 library to generate clean text reports (e.g., `db_report.md` or `tables_report.txt`).
* `export_to_excel.py` securely aggregates all application-specific SQLite tables and writes them onto discrete sheets into a master Excel file (`hostel_database_export.xlsx`).

### 3.9. Modular Dashboards Layouts
* Uses dedicated templates isolating complex logical flows to avoid monolithic dashboard components. For instance, Complaints and Fee Checkouts have their own isolated web pages, keeping the primary user dashboard minimalistic.

---

## 4. Database Schema Structure
The application revolves around relationally linked SQL entities under the `startpage` application namespace:

1. **`User` (Custom)**: Defines core credentials, roles (`ADMIN`, `STUDENT`), registration number, and department.
2. **`Hostel`**: Tracks `name`, `block`, `total_floors`, and `warden_name`.
3. **`Room`**: Links to `Hostel` (1-to-Many). Tracks `room_number`, `capacity`, `current_occupancy`, and `room_type` (AC/Non-AC). Includes database-level constraints testing capacity limits.
4. **`StudentProfile`**: Maps 1-to-1 with a User. Includes `year` of study, `guardian_phone`, `address`, and links to the `Room` they are assigned. 
5. **`Complaint`**: Links to `User` and optionally to a `Room`. Tracks `category`, `description`, `status` and resolution notes.
6. **`Fee`**: Links to `User`. Tracks financial records like `amount`, `semester`, and `payment_status`.
7. **`Outpass`**: Links to `User`. Tracks leave variables, `dates`, and `status`.
8. **`MessMenu`**: Unrelated scheduling table tracking daily food structures. 

---

## 5. Potential Use Cases
This project serves as a perfect candidate for:
* **Academic Portfolios / DBMS Courses**: An exemplary end-to-end relational database management system showing how tables communicate. 
* **Small-to-Medium Hostels**: Viable initial infrastructure for a college to move away from tedious paper methodologies toward a dynamic, digital solution.

---

## 6. Implementation Reference

### 6.1 Front End Via HTML/CSS & Django Templates :

**hostelsys_redesign.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HostelSys</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600&family=Gloock:ital@1&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
<style>
  :root {
    --bg-deep:    #0e0618;
    --bg-card:    #261740;
    --accent-rose: #e8608a;
    --accent-violet: #8b6be8;
    --text-primary: #f4eeff;
    --border-subtle: rgba(180,140,255,0.12);
  }

  body {
    background: var(--bg-deep);
    color: var(--text-primary);
    font-family: 'DM Sans', system-ui, sans-serif;
  }

  .auth-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 24px;
    padding: 2.8rem;
    position: relative;
    overflow: hidden;
  }
  
  .panel { display: none; }
  .panel.active { display: block; animation: flipIn 0.28s ease forwards; }

  @keyframes flipIn {
    from { opacity: 0; transform: translateY(10px) scale(0.98); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
  }
</style>
</head>
<body>

<main class="page">
  <!-- Interactive Tab Navigation -->
  <div class="tab-switcher" role="tablist">
    <button class="tab-btn active" onclick="switchPanel('login', this)">Sign In</button>
    <button class="tab-btn" onclick="switchPanel('signup', this)">Register</button>
  </div>

  <!-- Django Form Integration -->
  <div id="panel-login" class="panel active">
    <div class="auth-card">
      <form method="post" action="{% url 'login_admin' %}" id="login-form">
        {% csrf_token %}
        <input type="hidden" name="role" id="role-field" value="admin">
        
        <div class="form-field">
          <label class="form-label">Username</label>
          <div class="input-wrap">
            <i class="bi bi-person input-icon"></i>
            <input type="text" name="username" required>
          </div>
        </div>
        
        <button type="submit" class="btn-submit" id="login-btn">Sign in</button>
      </form>
    </div>
  </div>
</main>

<script>
  // Vanilla JavaScript for Frontend Interactivity
  function switchPanel(name, btn) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    const panel = document.getElementById('panel-' + name);
    if (panel) { panel.classList.add('active'); }
    if (btn && btn.classList) btn.classList.add('active');
  }
</script>
</body>
</html>
```
