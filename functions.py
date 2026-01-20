#1️⃣ Simple Function (No Parameters)
def greet():
    print("Hello, welcome to Python!")

greet()


#2️⃣ Function with Parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum =", result)

#3️⃣ Function with User Input
def find_square(num):
    return num * num

n = int(input("Enter number: "))
print("Square =", find_square(n))

#4️⃣ Function with Default Argument
def greet(name="User"):
    print("Hello", name)

greet()
greet("Jeremia")

#5️⃣ Function with Multiple Return Values
def calculator(a, b):
    return a+b, a-b, a*b

add, sub, mul = calculator(10, 5)
print(add, sub, mul)

#6️⃣ Function with Keyword Arguments
def student(name, course):
    print("Name:", name)
    print("Course:", course)

student(course="Networking", name="Alice")

#7️⃣ Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

#8️⃣ Lambda (Anonymous) Function
square = lambda x: x * x
print(square(4))

#9️⃣ Function Using List
def find_max(numbers):
    return max(numbers)

nums = [10, 45, 23, 89]
print("Max =", find_max(nums))

#🔥 Practical Exam Example
def is_pass(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(is_pass(78))
print(is_pass(45))


#✅ Program: Student Management System
students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully.\n")

def display_students():
    if not students:
        print("No students found.\n")
        return
    print("Student List:")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}")
    print()

def calculate_average():
    if not students:
        print("No students to calculate average.\n")
        return
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print("Average marks:", avg, "\n")

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average Marks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")

