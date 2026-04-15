# Database Tables Report

Below is the output of all the application specific tables stored in sqlite3.

## Table: startpage_hostel

|   id | name              | block   |   total_floors | warden_name   | created_at                 | updated_at                 |
|-----:|:------------------|:--------|---------------:|:--------------|:---------------------------|:---------------------------|
|    1 | Main Boys Hostel  | A       |              3 | Mr. Warden    | 2026-03-16 07:39:34.080707 | 2026-03-16 07:39:34.080781 |
|    2 | Chellammal        | Girls   |              4 | TBD           | 2026-03-30 07:36:49.327185 | 2026-03-30 07:36:49.327221 |
|    3 | Sivasakthi Hostel | Girls   |              4 | TBD           | 2026-03-30 07:36:49.341882 | 2026-03-30 07:36:49.341909 |
|    4 | Boys Hostel 2     | Boys    |              4 | TBD           | 2026-03-30 07:36:49.349354 | 2026-03-30 07:36:49.349389 |
|    5 | OMV               | Boys    |              4 | TBD           | 2026-03-30 07:36:49.358445 | 2026-03-30 07:36:49.358472 |
|    6 | Main Girls Hostel | B       |              2 | Mrs. Gupta    | 2026-04-07 16:43:14.966425 | 2026-04-07 16:43:14.966456 |

## Table: startpage_user

|   id | password                                                                                  | last_login                 |   is_superuser | username             | first_name      | last_name   | email                   |   is_staff |   is_active | date_joined                | role    | register_number   | phone   | created_at                 | updated_at                 | department   |
|-----:|:------------------------------------------------------------------------------------------|:---------------------------|---------------:|:---------------------|:----------------|:------------|:------------------------|-----------:|------------:|:---------------------------|:--------|:------------------|:--------|:---------------------------|:---------------------------|:-------------|
|    1 | pbkdf2_sha256$1200000$Geo4dD7DSMitoZPiR5F6K6$7R7cSxV2lU9kZyIyMI4l+inDefLpc8crls/ekOneLws= | 2026-03-30 08:12:48.420652 |              1 | testadmin            |                 |             | testadmin@example.com   |          1 |           1 | 2026-03-16 07:39:31.439235 | ADMIN   |                   |         | 2026-03-16 07:39:32.743733 | 2026-03-30 07:26:45.679604 | CSE          |
|    2 | pbkdf2_sha256$1200000$NA9WZCherTQbw0EOsu2oBz$pO4mkuBE5OnzmYoXoXNvg9uw080ZZf6ffVMhHn2Rtjs= | 2026-03-30 08:25:16.375250 |              0 | sr1070@srmist.edu.in | Test            | Student     | sr1070@srmist.edu.in    |          0 |           1 | 2026-03-16 07:39:32.772931 | STUDENT | SR1070            |         | 2026-03-16 07:39:34.062385 | 2026-03-16 07:39:34.062404 | CSE          |
|    3 | pbkdf2_sha256$1200000$JayPWrxQGsBF5F2jrJP3kY$+D1zoUuE5FBwlb+ixuNvPIEH78Cqy3k6Sc3fVevimBE= | 2026-03-16 08:38:50.517140 |              0 | thamu                | Thamaraishree M |             | tm7195@srmist.edu.in    |          0 |           1 | 2026-03-16 08:38:40.893225 | STUDENT | RA2411003020023   |         | 2026-03-16 08:38:42.316932 | 2026-03-16 08:38:42.316945 | MECH         |
|    4 | pbkdf2_sha256$1200000$hSU6TGpvVsrPLGKF83NNI5$voeyyCHuX54MkLArz69Bam8eowKL1EmwbSp+arwSiJA= | 2026-03-30 08:24:19.798209 |              1 | mechadmin            |                 |             | mechadmin@example.com   |          1 |           1 | 2026-03-16 08:49:09.813275 | ADMIN   |                   |         | 2026-03-16 08:49:11.035246 | 2026-03-30 07:35:27.720226 | MECH         |
|    5 | pbkdf2_sha256$1200000$xPgL0rFqFukEqNJjvxCJpT$V6suJNna0nQ+XpPXxtxEvqIVzxtdcksLIEi663kFe+0= | 2026-03-30 07:29:26.173710 |              0 | kindasindhu          | R Sindhu        |             | sindhusree017@gmail.com |          0 |           1 | 2026-03-30 07:29:12.850423 | STUDENT | RA2727282991      |         | 2026-03-30 07:29:14.196685 | 2026-03-30 07:29:14.196698 | MECH         |
|    6 | pbkdf2_sha256$1200000$6zaUmENDFXHI6hhytfRRo1$jjctfi/BoxZlD2r1ABTAijWsgM28xmVNBVsb9e6NPBk= |                            |              1 | mechadmin123         |                 |             | mechadmin@gmail.com     |          1 |           1 | 2026-03-30 07:35:12.753385 | STUDENT |                   |         | 2026-03-30 07:35:13.985465 | 2026-03-30 07:35:13.985481 |              |
|    7 | pbkdf2_sha256$1200000$BeURTfeFfVbDwwDtEDzJjL$6t4ir+WjCBusqKiw+QjHAGD+J3BPj/E0hH8/oCMLA0c= | 2026-03-30 07:45:12.093859 |              1 | itadmin              |                 |             | itadmin@gmail.com       |          1 |           1 | 2026-03-30 07:43:59.845178 | STUDENT |                   |         | 2026-03-30 07:44:01.109830 | 2026-03-30 07:44:01.109849 | IT           |
|    8 | pbkdf2_sha256$1200000$8sH6UAyIdmYEKk86SQeW5U$9i0rJhzpBfmM8KfethalF1XnolMNMImsvxOXBx6AF2o= | 2026-03-30 08:19:24.769276 |              1 | cseadmin             |                 |             | cseadmin@gmail.com      |          1 |           1 | 2026-03-30 08:13:48.945715 | STUDENT |                   |         | 2026-03-30 08:13:50.166876 | 2026-03-30 08:13:50.166893 | CSE          |
|    9 | pbkdf2_sha256$1200000$6MLgM6zlX4hfb4TtPI48UD$7GI4mjQVgWKPWRD38ZWg4TsBJl2pLiaIzHDy9u6hSI0= | 2026-03-30 08:17:58.453674 |              0 | varunika123          | Varunika P A    |             | varunikapa55@gmail.com  |          0 |           1 | 2026-03-30 08:15:47.831307 | STUDENT | RA2411003020018   |         | 2026-03-30 08:15:49.133163 | 2026-03-30 08:15:49.133176 | CSE          |
|   10 | pbkdf2_sha256$1200000$6Oe8Y95eu153SZV8qkwtgO$aLuwsTkPbw6a9SDMu9jARQUlc3NCClFwYP84kEpgnOQ= |                            |              0 | alice@srmist.edu.in  | Alice           | Smith       | alice@srmist.edu.in     |          0 |           1 | 2026-04-07 16:43:14.996335 | STUDENT | SR1071            |         | 2026-04-07 16:43:16.235469 | 2026-04-07 16:43:16.235481 | ECE          |
|   11 | pbkdf2_sha256$1200000$jEbbE8m1hMwz96mzdHZyor$dBEUwX5m4+ZjVcaZYMK7RfK44c4n6CotEWbqqpKe7QQ= |                            |              0 | bob@srmist.edu.in    | Bob             | Johnson     | bob@srmist.edu.in       |          0 |           1 | 2026-04-07 16:43:16.275901 | STUDENT | SR1072            |         | 2026-04-07 16:43:17.347568 | 2026-04-07 16:43:17.347576 | MECH         |

## Table: startpage_user_groups

*No data in this table.*

## Table: startpage_user_user_permissions

*No data in this table.*

## Table: startpage_fee

|   id |   amount | semester    | payment_status   | paid_on    | created_at                 | updated_at                 |   student_id |
|-----:|---------:|:------------|:-----------------|:-----------|:---------------------------|:---------------------------|-------------:|
|    1 |    25000 | Spring 2026 | PAID             | 2026-01-15 | 2026-04-07 16:43:16.258684 | 2026-04-07 16:43:16.258706 |           10 |
|    2 |    20000 | Spring 2026 | PENDING          |            | 2026-04-07 16:43:17.366929 | 2026-04-07 16:43:17.366958 |           11 |

## Table: startpage_complaint

|   id | category    | description                  | status      | admin_note                           | ai_recommendation                              | created_at                 | updated_at                 |   student_id |   room_id |
|-----:|:------------|:-----------------------------|:------------|:-------------------------------------|:-----------------------------------------------|:---------------------------|:---------------------------|-------------:|----------:|
|    1 | Maintenance | Fan is not working properly. | IN_PROGRESS | An Electrician will come on March 23 | Schedule maintenance team review within 24hrs. | 2026-03-16 07:39:34.113473 | 2026-03-16 07:50:22.816691 |            2 |         1 |
|    2 | Electrical  | Tubelight is flickering.     | PENDING     |                                      |                                                | 2026-04-07 16:43:17.372116 | 2026-04-07 16:43:17.372135 |           11 |         1 |

## Table: startpage_studentprofile

|   id | department   | year     |   guardian_phone | address          | created_at                 | updated_at                 |   room_id |   user_id |
|-----:|:-------------|:---------|-----------------:|:-----------------|:---------------------------|:---------------------------|----------:|----------:|
|    1 | CSE          | 2nd Year |       1234567890 | 123 Main St      | 2026-03-16 07:39:34.104228 | 2026-03-16 07:49:46.821740 |       nan |         2 |
|    2 | MECH         | 1st Year |                  |                  | 2026-03-16 08:38:42.335665 | 2026-03-16 08:38:42.335702 |       nan |         3 |
|    3 | MECH         | 1st Year |                  |                  | 2026-03-30 07:29:14.205204 | 2026-03-30 07:29:14.205244 |       nan |         5 |
|    4 | CSE          | 1st Year |                  |                  | 2026-03-30 08:15:49.147341 | 2026-03-30 08:15:49.147379 |       nan |         9 |
|    5 | ECE          | 1st Year |       9876543210 | 123 Maple Street | 2026-04-07 16:43:16.250324 | 2026-04-07 16:43:16.250348 |         2 |        10 |
|    6 | MECH         | 3rd Year |       5551234567 | 456 Oak Avenue   | 2026-04-07 16:43:17.361000 | 2026-04-07 16:43:17.361020 |         1 |        11 |

## Table: startpage_room

|   id | room_number   |   capacity |   current_occupancy | room_type   | created_at                 | updated_at                 |   hostel_id |
|-----:|:--------------|-----------:|--------------------:|:------------|:---------------------------|:---------------------------|------------:|
|    1 | A101          |          2 |                   0 | NON_AC      | 2026-03-16 07:39:34.092945 | 2026-03-16 07:39:34.092971 |           1 |
|    2 | B101          |          3 |                   2 | AC          | 2026-04-07 16:43:14.977701 | 2026-04-07 16:43:14.977725 |           6 |
|    3 | A102          |          2 |                   0 | AC          | 2026-04-07 16:43:14.986448 | 2026-04-07 16:43:14.986478 |           1 |

## Table: startpage_messmenu

|   id | day   | breakfast              | lunch                                      | snacks        | dinner                       |
|-----:|:------|:-----------------------|:-------------------------------------------|:--------------|:-----------------------------|
|    1 | MON   | Dosa, Chutney, Sambhar | Rice, Dal, Mixed Veg Curry                 | Samosa, Tea   | Chapati, Paneer Sabzi, Rice  |
|    2 | TUE   | Idli, Vada, Sambhar    | Rice, Rajma, Aloo Gobi                     | Puff, Coffee  | Poori, Chana Masala, Rice    |
|    3 | WED   | Poha, Jalebi           | Rice, Chicken Curry / Paneer Butter Masala | Biscuits, Tea | Chapati, Dal Tadka, Rice     |
|    4 | THU   | Aloo Paratha, Curd     | Veg Biryani, Raita                         | Bonda, Tea    | Chapati, Mix Veg, Rice       |
|    5 | FRI   | Upma, Kesari Bath      | Rice, Sambhar, Rasam, Fish Fry/Gobi 65     | Cake, Coffee  | Chapati, Egg Curry/Dal, Rice |
|    6 | SAT   | Masala Dosa, Chutney   | Rice, Dal Makhani                          | Pav Bhaji     | Fried Rice, Manchurian       |
|    7 | SUN   | Chole Bhature          | Chicken Biryani / Veg Pulao                | Pakora, Tea   | Chapati, Dal, Rice           |

## Table: startpage_outpass

|   id | destination          | reason                 | from_date   | to_date    | status   | admin_note                                             | created_at                 | updated_at                 |   student_id |
|-----:|:---------------------|:-----------------------|:------------|:-----------|:---------|:-------------------------------------------------------|:---------------------------|:---------------------------|-------------:|
|    1 | Coimbatore           | Going Home for Weekend | 2026-03-21  | 2026-03-23 | REJECTED | We have classes on Saturday. Submit a letter tomorrow. | 2026-03-16 08:02:35.560716 | 2026-03-16 08:03:59.847115 |            2 |
|    2 | Coimbatore           | Weekend Holidays       | 2026-03-27  | 2026-03-31 | APPROVED |                                                        | 2026-03-23 08:34:15.648886 | 2026-03-30 08:23:56.367472 |            2 |
|    3 | Local Guardian House | Weekend Discharged     | 2026-04-10  | 2026-04-12 | APPROVED |                                                        | 2026-04-07 16:43:16.265811 | 2026-04-07 16:43:16.265834 |           10 |

