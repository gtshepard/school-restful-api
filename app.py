from flask import Flask, jsonify
from flask import abort, make_response
from flask import request
import sys
import psycopg2

hostname = 'localhost'
username = 'garrison'
password = 'Gt$092894'
database = 'myschool'

app = Flask(__name__)
my_connection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
current = my_connection.cursor()

#CREATE
@app.route('/school/api/v1.0/students/', methods=['POST'])
def create_student():
    student = {
        'student_id':request.json['student_id'],
        'first_name':request.json['first_name'],
        'last_name':request.json['last_name'], 
        'address':request.json['address'],
        'email':request.json['email']
    }

    current.execute("INSERT INTO Student (student_id, first_name, last_name, address, email) VALUES ('%s', '%s', '%s','%s', '%s')" % (student['student_id'],student['first_name'],student['last_name'], student['address'], student['email']))
   
    my_connection.commit()
    return jsonify({"student":student})

@app.route('/school/api/v1.0/courses/', methods=['POST'])
def create_course():
    course = {
        'course_id':request.json['course_id'],    
        'name':request.json['name']
    } 
    current.execute("INSERT INTO course (course_id, name) VALUES('%s','%s')"%(course['course_id'], course['name']))
    my_connection.commit()
    return jsonify({"course":course})

@app.route('/school/api/v1.0/take_course/', methods=['POST'])
def take_course():
    take_course = {
        'student_id':request.json['student_id'],
        'course_id':request.json['course_id'],
        'grade':request.json['grade']
    }
    current.execute("INSERT INTO Takes (student_id, course_id, grade) VALUES('%s','%s','%s')" % (take_course['student_id'], take_course['course_id'], take_course['grade']))
    my_connection.commit()
    return jsonify({"take_course":take_course})

#READ
@app.route('/school/api/v1.0/students', methods=['GET'])
def get_students():
    current.execute("SELECT * FROM student")
    db_response = current.fetchall()
    return jsonify({'students': db_response})

@app.route('/school/api/v1.0/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    current.execute("SELECT student_id, first_name, last_name, address, email FROM student WHERE student_id='%s'" % student_id)
    db_response = current.fetchall()    
    return jsonify({'student':db_response})

@app.route('/school/api/v1.0/courses', methods=['GET'])
def get_courses():
    current.execute("SELECT * FROM course")
    db_response = current.fetchall()
    return jsonify({'courses':db_response})

@app.route('/school/api/v1.0/roster/<int:course_id>', methods=['GET'])
def get_course_roster(course_id):
    current.execute("SELECT s.student_id, last_name FROM takes t INNER JOIN student s ON s.student_id = t.student_id WHERE t.course_id='%s'" % course_id)

    db_response = current.fetchall()
    return jsonify({'roster':db_response})

@app.route('/school/api/v1.0/student_courses/<int:student_id>', methods=['GET'])
def get_student_courses(student_id):
    current.execute("SELECT c.course_id, name FROM takes t INNER JOIN course c ON c.course_id = t.course_id WHERE t.student_id='%s'" % student_id)
    db_response = current.fetchall()
    return jsonify({'roster':db_response})

#UPDATE
@app.route('/school/api/v1.0/students/<int:student_id>', methods=['PUT'])
def update_student_address(student_id):

    student = {
        'address':request.json['address']
    }

    current.execute("UPDATE Student SET address = '%s' WHERE student_id = '%s'"
                    % (student['address'], student_id))
    my_connection.commit()
    return jsonify({"student":student})

@app.route('/school/api/v1.0/courses/<int:course_id>', methods=['PUT'])
def update_course_name(course_id):
    course = {
        "name":request.json['name']
    }
    current.execute("UPDATE course SET name='%s' WHERE course_id='%s'"%(course['name'], course_id))
    my_connection.commit()
    return jsonify({'course':course})

@app.route('/school/api/v1.0/takes_courses/<int:student_id>/<int:course_id>', methods=['PUT'])
def update_grade(student_id, course_id):
    takes_course = {
        'grade':request.json['grade']
    }
    current.execute("UPDATE Takes SET grade='%s' WHERE student_id ='%s' AND course_id='%s';" % (takes_course['grade'], student_id, course_id))
    my_connection.commit()
    return jsonify({'takes_course':takes_course})

#DELETE
@app.route('/school/api/v1.0/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    current.execute("DELETE FROM Student WHERE student_id='%s'" % student_id)
    my_connection.commit()
    return jsonify({'result':True})

@app.route('/school/api/v1.0/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    current.execute("DELETE FROM Course WHERE course_id='%s'" % course_id)
    my_connection.commit()
    return jsonify({'result':True})

@app.route('/school/api/v1.0/takes_courses/<int:student_id>/<int:course_id>', methods=['DELETE'])
def delete_enrollment(student_id, course_id):
    current.execute("DELETE FROM Takes WHERE student_id='%s' AND course_id='%s'"%(student_id, course_id))
    my_connection.commit()
    return jsonify({'result':True})


