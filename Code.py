from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sumit",
  password="root",
  database="assignment"
)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sumit:root@localhost/assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    courses = db.relationship('Course', secondary='student_course', backref='students')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    courses = db.relationship('Course', backref='instructor')

student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
