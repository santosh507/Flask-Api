from flask import jsonify, abort
from wsgi.logger import app_logger, logger_obj
from wsgi.myApi.models import Employee
from wsgi import db
from flask import request
import sqlalchemy
import requests


@logger_obj.log_func_time
def employees():
    if request.method == "GET":
        # Get All Employees
        emp_list = Employee.get_all()
        data = [emp_obj.serialize for emp_obj in emp_list]
        return jsonify({"status": "success", "data": data}), 200
    elif request.method == "POST":
        # Create New Employee
        emp_obj = Employee(request.json["emp_id"], request.json["name"], request.json["role"], request.json["salary"])
        try:
            emp_obj.save()
        except sqlalchemy.exc.IntegrityError as ie:
            return jsonify({"status": "failure", "message": f"{ie.orig}"}), 409
        return jsonify({"status": "success", "message": f"Employee '{request.json['name']}' added successfully"}), 201
    abort(404)


def employee(emp_id):
    emp_obj = Employee.get_by_id(emp_id)
    if request.method == "GET":
        if not emp_obj:
            return jsonify({"status": "failure", "message": f"Employee with id '{emp_id}' not found "}), 404
        return jsonify({"status": "success", "data": emp_obj.serialize}), 200
    if request.method == "PUT":
        if not emp_obj:
            return jsonify({"status": "failure", "message": f"Employee with id '{emp_id}' not found for update"}), 404
        emp_obj.name = request.json["name"]
        emp_obj.salary = request.json["salary"]
        emp_obj.emp_id = request.json["emp_id"]
        emp_obj.role = request.json["role"]
        db.session.commit()
        return jsonify({"status": "success", "message": f"Employee with id '{emp_id}' updated successfully"}), 200
    if request.method == "DELETE":
        if not emp_obj:
            return jsonify({"status": "failure", "message": f"Employee with id '{emp_id}' not found for delete"}), 404
        emp_obj.delete()
        return jsonify({"status": "success", "message": f"Employee '{emp_obj.name}' deleted successfully"}), 200
    abort(404)

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


def get_user():
    resp_user = requests.get("https://reqres.in/api/users?page=2")
    resp_unknown = requests.get("https://reqres.in/api/unknown")
    total_page = resp_user.json()["total_pages"]
    per_page = resp_user.json()["per_page"]
    current_page = resp_user.json()["page"]
    user_page = "Total user Pages {}, Per Page {}, Current page {}".format(resp_user.json()["total_pages"],
                                                                           resp_user.json()["per_page"],
                                                                           resp_user.json()["page"])
    unknown = "Total unknown Pages {}, Per Page {}, Current page {}".format(resp_unknown.json()["total_pages"],
                                                                            resp_unknown.json()["per_page"],
                                                                            resp_unknown.json()["page"])
    return user_page, unknown
