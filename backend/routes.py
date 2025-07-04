from flask import Blueprint, request, jsonify
from models import Employee
from config import db

api = Blueprint('api', __name__)

@api.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': e.id,
        'name': e.name,
        'department': e.department,
        'email': e.email
    } for e in employees]), 200

@api.route('/employees', methods=['POST'])
def create_or_update_employee():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    employee = Employee.query.filter_by(email=data['email']).first()
    if employee:
        employee.name = data.get('name', employee.name)
        employee.department = data.get('department', employee.department)
        message = 'Employee updated'
    else:
        employee = Employee(**data)
        db.session.add(employee)
        message = 'Employee created'

    db.session.commit()
    return jsonify({'message': message}), 200
