import pickle
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

emp = Employee("Deepak", 20, 50000)

with open("employee.pickle", 'wb') as file:
    pickle.dump(emp, file)

with open("employee.pickle", 'rb') as file:
    emp_loaded = pickle.load(file)

print(emp_loaded.name)
print(emp_loaded.age)
print(emp_loaded.salary)
