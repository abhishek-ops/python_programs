class employee1():
    def __init__(self,emp_name,age):
        self.emp_name = emp_name
        self.age = age


class employee2(employee1):
    def __init__(self,emp_name,age,emp_id):
        self.emp_name = emp_name
        self.age = age
        self.emp_id = emp_id


class child_employee(employee2):
    def __init__(self,emp_name,age,emp_id):
        self.emp_name = emp_name
        self.age = age
        self.emp_id = emp_id

emp1=child_employee('Mayank',23,101)
emp2=employee2('rahul',25,102)


print(emp1.emp_id)
print(emp2.emp_name)
