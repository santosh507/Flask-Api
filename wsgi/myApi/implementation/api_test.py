from flask import jsonify
from wsgi.logger import app_logger
from wsgi.myApi.models import Employee
from wsgi import db
from flask import request


def get_employees():
    emp_list = Employee.query.all()
    data = [emp_obj.serialize for emp_obj in emp_list]
    return jsonify({"status": "success", "data": data})


def get_employee(id):
    emp_obj = Employee.query.filter_by(id=id).first()
    return jsonify({"status": "success", "data": emp_obj.serialize})


def add_employee():
    emp_obj = Employee(request.json["emp_id"], request.json["name"], request.json["role"], request.json["salary"])
    db.session.add(emp_obj)
    db.session.commit()
    return jsonify({"status": "success", "message": f"Employee '{request.json['name']}' added successfully"})


def update_employee(id):
    emp_obj = Employee.query.filter_by(id=id).first()
    emp_obj.name = request.json["name"]
    emp_obj.salary = request.json["salary"]
    emp_obj.emp_id = request.json["emp_id"]
    emp_obj.role = request.json["role"]
    db.session.commit()
    return jsonify({"status": "success", "message": f"Employee '{request.json['name']}' updated successfully"})


def delete_employee(id):
    emp_obj = Employee.query.filter_by(id=id).first()
    db.session.delete(emp_obj)
    db.session.commit()
    return jsonify({"status": "success", "message": f"Employee '{emp_obj.name}' deleted successfully"})

    #
    # class Employee:
    #     raise_amt = 1
    #
    #     def __init__(self, name, salary, role):
    #         self.name = name
    #         self.salary = salary
    #         self.role = role
    #
    #     def __repr__(self):
    #         return "Employee({}, {}, {})".format(self.name, self.salary, self.role)
    #
    #     def apply_raise(self):
    #         self.salary = self.salary * self.raise_amt
    #
    #     @classmethod
    #     def alter_raise(cls, new_raise_amnt):
    #         cls.raise_amt = new_raise_amnt
    #
    #
    # emp1 = Employee("Santosh Hegde", 50000, "Python Developer")
    # emp1.apply_raise()
    # app_logger.info(emp1.__dict__)
    # app_logger.info(emp1)
    # Employee.alter_raise(1.04)
    # emp1.apply_raise()
    # app_logger.info(emp1)
