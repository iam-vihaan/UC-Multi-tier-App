from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///employees.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Replace with a secure key in production

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))
    email = db.Column(db.String(100))

# Dummy user for authentication
USERS = {
    "admin": "password123"
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if USERS.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad credentials"}), 401

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': e.id,
        'name': e.name,
        'department': e.department,
        'email': e.email
    } for e in employees])

@app.route('/api/employees', methods=['POST'])
@jwt_required()
def create_employee():
    data = request.json
    employee = Employee(**data)
    db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee created'}), 201

@app.route('/api/employees/<int:emp_id>', methods=['PUT'])
@jwt_required()
def update_employee(emp_id):
    data = request.json
    employee = Employee.query.get(emp_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    employee.name = data.get('name', employee.name)
    employee.department = data.get('department', employee.department)
    employee.email = data.get('email', employee.email)
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

@app.route('/api/employees/<int:emp_id>', methods=['DELETE'])
@jwt_required()
def delete_employee(emp_id):
    employee = Employee.query.get(emp_id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
