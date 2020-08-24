import unittest
from wsgi import create_app
from wsgi.myApi.models import Employee


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


if __name__ == "__main__":
    unittest.main()
