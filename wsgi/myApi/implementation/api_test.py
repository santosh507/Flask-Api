from flask import jsonify
from wsgi.logger import app_logger


def test_api():
    app_logger.debug("Testing testApi endpoint View")
    app_logger.info("In testApi endpoint View")
    return jsonify({"Message": "Hello World"})


def test_api_clone():
    app_logger.debug("Testing testApiClone endpoint View")
    app_logger.info("In testApiClone endpoint View")
    return jsonify({"Message": "Hello World"})

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
