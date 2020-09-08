import unittest
from wsgi import create_app
from wsgi.myApi.models import Employee
from unittest.mock import patch, Mock, MagicMock
from wsgi.myApi.implementation.api_test import get_user
import requests

def mocked_requests_get(*args, **kwargs):
    new_mock = Mock()
    new_mock.return_value.status_code = 200
    new_mock.return_value.json.return_value = []

    if args[0] == "https://reqres.in/api/users?page=2":
        data = {"page": 2, "per_page": 6, "total": 12, "total_pages": 2,
                "data": [
                    {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"},
                    {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg"},
                    {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"},
                    {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"},
                    {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"},
                    {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
                     "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"}],
                "ad": {"company": "StatusCode Weekly", "url": "http://statuscode.org/",
                       "text": "A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."}}
        new_mock.return_value.status_code = 200
        new_mock.return_value.json.return_value = data
    if args[0] == "https://reqres.in/api/unknown":
        data = {"page": 1, "per_page": 6, "total": 12, "total_pages": 2,
                "data": [{"id": 1, "name": "cerulean", "year": 2000, "color": "#98B2D1", "pantone_value": "15-4020"},
                         {"id": 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375",
                          "pantone_value": "17-2031"},
                         {"id": 3, "name": "true red", "year": 2002, "color": "#BF1932", "pantone_value": "19-1664"},
                         {"id": 4, "name": "aqua sky", "year": 2003, "color": "#7BC4C4", "pantone_value": "14-4811"},
                         {"id": 5, "name": "tigerlily", "year": 2004, "color": "#E2583E", "pantone_value": "17-1456"},
                         {"id": 6, "name": "blue turquoise", "year": 2005, "color": "#53B0AE",
                          "pantone_value": "15-5217"}],
                "ad": {"company": "StatusCode Weekly", "url": "http://statuscode.org/",
                       "text": "A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things."}}
        new_mock.return_value.status_code = 200
        new_mock.return_value.json.return_value = data
    return new_mock.return_value


class TestMyApi(unittest.TestCase):
    app = create_app()
    client = app.test_client()

    @classmethod
    def setUpClass(cls):
        with cls.app.app_context():
            emp_obj = Employee.get_by_id("abhiheg")
            try:
                Employee.delete(emp_obj)
            except Exception as del_err:
                pass

    def test_1_config(self):
        self.assertTrue(self.app.config["DEBUG"])

    def test_2_employees_list(self):
        resp = self.client.get("/api/employee")
        self.assertEqual(200, resp.status_code)
        resp_found = self.client.get("/api/employee/abhiheg")
        self.assertEqual(404, resp_found.status_code)

    def test_3_create_employee(self):
        emp = {"emp_id": "abhiheg", "name": "Abhishek Hegde", "role": "Student", "salary": "0"}
        resp = self.client.post("/api/employee", json=emp)
        self.assertEqual(201, resp.status_code)
        resp_dup = self.client.post("/api/employee", json=emp)
        self.assertEqual(409, resp_dup.status_code)
        resp_found = self.client.get("/api/employee/abhiheg")
        self.assertEqual(200, resp_found.status_code)

    def test_4_update_employee(self):
        emp = {"emp_id": "abhiheg", "name": "Abhishek Hegde", "role": "BCA", "salary": "0"}
        resp = self.client.put("/api/employee/abhiheg", json=emp)
        self.assertEqual(200, resp.status_code)
        resp_found = self.client.get("/api/employee/abhiheg")
        self.assertEqual(200, resp_found.status_code)

    def test_5_delete_employee(self):
        resp = self.client.delete("/api/employee/abhiheg")
        self.assertEqual(200, resp.status_code)
        resp_found = self.client.get("/api/employee/abhiheg")
        self.assertEqual(404, resp_found.status_code)

    # @patch("wsgi.myApi.implementation.api_test.requests.get")
    # def test_sample_get(self, mock_get_user):
    #     data = {'page': 2,
    #             'per_page': 6,
    #             'total': 12,
    #             'total_pages': 2,
    #             'data': [{'id': 7,
    #                       'email': 'michael.lawson@reqres.in',
    #                       'first_name': 'Michael',
    #                       'last_name': 'Lawson',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg'},
    #                      {'id': 8,
    #                       'email': 'lindsay.ferguson@reqres.in',
    #                       'first_name': 'Lindsay',
    #                       'last_name': 'Ferguson',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg'},
    #                      {'id': 9,
    #                       'email': 'tobias.funke@reqres.in',
    #                       'first_name': 'Tobias',
    #                       'last_name': 'Funke',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg'},
    #                      {'id': 10,
    #                       'email': 'byron.fields@reqres.in',
    #                       'first_name': 'Byron',
    #                       'last_name': 'Fields',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg'},
    #                      {'id': 11,
    #                       'email': 'george.edwards@reqres.in',
    #                       'first_name': 'George',
    #                       'last_name': 'Edwards',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg'},
    #                      {'id': 12,
    #                       'email': 'rachel.howell@reqres.in',
    #                       'first_name': 'Rachel',
    #                       'last_name': 'Howell',
    #                       'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg'}],
    #             'ad': {'company': 'StatusCode Weekly',
    #                    'url': 'http://statuscode.org/',
    #                    'text': 'A weekly newsletter focusing on software development, infrastructure, the server, performance, and the stack end of things.'}}
    #     mock_get_user.return_value.status_code = 200
    #     mock_get_user.return_value.json.return_value = data
    #     resp = get_user()
    #     print(resp)
    #     self.assertEqual(resp, "Total Pages 2, Per Page 6, Current page 2")

    @patch("wsgi.myApi.implementation.api_test.requests.get", side_effect=mocked_requests_get)
    def test_sample_get(self, mock_get):
        # def test_sample_get(self):
        # mock_get_user.return_value =
        print(mock_get.return_value.json.return_value)
        resp = get_user()
        print(resp)
        # self.assertEqual(resp, "Total Pages 2, Per Page 6, Current page 2")


if __name__ == "__main__":
    unittest.main()
