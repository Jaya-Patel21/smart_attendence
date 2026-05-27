from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
              
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        attendance INTEGER
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    roll = request.form['roll']
    attendance = int(request.form['attendance'])  # FIXED

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, roll, attendance) VALUES (?, ?, ?)",
        (name, roll, attendance)
    )

    conn.commit()
    conn.close()

    return "Student Added Successfully"

@app.route('/students')
def students():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    
    return render_template("students.html", data=data)

@app.route('/predict/<int:attendance>')
def predict(attendance):

    if attendance < 75:
        return "<h2 style='color:red;'> Risk</h2>"
    else:
        return "<h2 style='color:green;'>Safe</h2>"

@app.route('/update/<int:id>')
def update(id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET attendance = 90 WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return "Updated Successfully"

@app.route('/delete/<int:id>')
def delete(id):

    if not id:
        return "Invalid ID"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return "Deleted Successfully"

if __name__ == '__main__':
    app.run(debug=True)