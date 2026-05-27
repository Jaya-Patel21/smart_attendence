Smart Attendance System
A simple Flask-based Smart Attendance System with CRUD operations and basic ML prediction.

Features:
 
Add Student
View Students
Delete Student
Update Attendance
Attendance Status Prediction
Safe 🟢
Shortage Risk 🔴
SQLite Database
Simple Bootstrap UI

🛠 Technologies Used
Python
Flask
SQLite
HTML
Bootstrap
Machine Learning Logic (Basic Prediction)


📂 Project Structure
smart_attendance/
│
├── app.py
├── database.db
├── templates/
│   ├── index.html
│   └── students.html
│
├── static/
│
└── model/


▶️ How to Run the Project
1️⃣ Install Flask
pip install flask
2️⃣ Run the Project
python app.py
3️⃣ Open Browser
http://127.0.0.1:5000


📊 ML Prediction Logic:

If attendance is below 75: Shortage Risk
Else:Safe

Functionalities
Add Student
Stores student details in SQLite database.
View Students

Displays:
Name
Roll Number
Attendance
Status
Delete Student
Delete any student record.
Update Attendance
Update attendance value from backend route.

Future Improvements:
Real Machine Learning Model
Login System
Dashboard UI
Charts & Analytics
Attendance Percentage Graph

Author
Jaya Patel

