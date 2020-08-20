from wsgi.myApi.url import myApi
from wsgi.myApi.implementation.api_test import get_employees, add_employee, get_employee, update_employee, \
    delete_employee

myApi.add_url_rule("/employee", "List Employees", get_employees, methods=["GET"])
myApi.add_url_rule("/employee/<int:id>", "List Employee by Id", get_employee, methods=["GET"])
myApi.add_url_rule("/employee", "add new employee", add_employee, methods=["POST"])
myApi.add_url_rule("/employee/<int:id>", "update employee", update_employee, methods=["PUT"])
myApi.add_url_rule("/employee/<int:id>", "delete an employee", delete_employee, methods=["DELETE"])
