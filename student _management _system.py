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
