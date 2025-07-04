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
    } for e in employees])

@api.route('/employees', methods=['POST'])
def update_employee():
    data = request.json
    employee = Employee.query.filter_by(email=data['email']).first()
    if employee:
        employee.name = data['name']
        employee.department = data['department']
    else:
        employee = Employee(**data)
        db.session.add(employee)
    db.session.commit()
    return jsonify({'message': 'Employee updated'})
