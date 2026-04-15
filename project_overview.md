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

### 3.5. Financial Tracking
* Manages the financial relationship between the hosteller and the hostel management. 
* Tracks varying fee amounts, corresponding semesters, and updates payment statuses (Paid, Pending, Overdue). 

### 3.6. Mess Menu
* An interactive database schedule detailing the food menu (Breakfast, Lunch, Snacks, Dinner) for each day of the week.

### 3.7. Internal Data Exporting & Reporting Tools
* A robust scripting backend dedicated to data analysis and extraction.
* Custom scripts heavily utilize Pandas and Python's built-in sqlite3 library to generate clean text reports (e.g., `db_report.md` or `tables_report.txt`).
* `export_to_excel.py` securely aggregates all application-specific SQLite tables and writes them onto discrete sheets into a master Excel file (`hostel_database_export.xlsx`).

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
