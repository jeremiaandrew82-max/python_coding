#Example Scenario: Employee Management System
#1️⃣ Base Class (Encapsulation)
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id          # public
        self.name = name              # public
        self._salary = salary         # protected variable

    def get_salary(self):
        return self._salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self._salary}")


#✔ Demonstrates encapsulation (data + methods together)

#2️⃣ Inheritance (Derived Class)
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self._salary}, Dept: {self.department}")


#✔ Manager inherits from Employee

#3️⃣ Polymorphism
def show_employee_details(employee):
    employee.display_info()


#✔ Same function, different behavior depending on object type

#4️⃣ Using the Classes

emp1 = Employee(1, "John", 50000)
mgr1 = Manager(2, "Alice", 80000, "IT")

show_employee_details(emp1)
show_employee_details(mgr1)


#SIMPLE OOP EXAMPLE (Very Common in Exams)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

s1 = Student("Mary", 78)
s2 = Student("John", 45)

s1.result()
s2.result()