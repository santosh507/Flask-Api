from wsgi import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    emp_id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80))
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.id} , {self.name}, {self.salary})"

    @property
    def serialize(self):
        return {"id": self.id, "name": self.name, "role": self.role, "salary": self.salary}
