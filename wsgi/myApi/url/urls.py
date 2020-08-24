from wsgi.myApi.url import myApi
from wsgi.myApi.implementation.api_test import employees, employee

myApi.add_url_rule("/employee", "List Employees", employees, methods=["GET", "POST"])
myApi.add_url_rule("/employee/<emp_id>", "List Employee by Id", employee, methods=["GET", "PUT", "DELETE"])
