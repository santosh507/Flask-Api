from wsgi import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    emp_id = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=True)
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.id} , {self.name}, {self.salary}, {self.emp_id}, {self.role})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, emp_id):
        return cls.query.filter_by(emp_id=emp_id).first()

    @property
    def serialize(self):
        return {"id": self.id, "name": self.name, "emp_id": self.emp_id, "role": self.role, "salary": self.salary}
