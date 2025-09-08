from flask import Flask, jsonify, request
import mysql.connector as mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mycon = mysql.connect(host= "localhost", user = "root", password = "0129", database = "login")
cursor = mycon.cursor()

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    course = data.get('course')
    query = "INSERT into student_form (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    mycon.commit()
    return jsonify({"message": "Data inserted successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
