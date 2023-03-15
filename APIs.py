from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sumit'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'assignment'
mysql = MySQL(app)
CORS(app)

# Route to get all students
@app.route('/students')
def get_students():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Students")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# Route to get all courses
@app.route('/courses')
def get_courses():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Courses")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

# Route to get all instructors
@app.route('/instructors')
def get_instructors():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Instructor")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

    if __name__ == '__main__':
        app.run(debug=True)
