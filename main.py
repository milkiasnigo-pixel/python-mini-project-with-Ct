# Student Grade Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students[name] = grade
    print(f"{name} added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    
    print("\nStudent List:")
    for name, grade in students.items():
        print(f"{name}: {grade}")
    print()

def calculate_average():
    if not students:
        print("No data to calculate average.\n")
        return
    
    avg = sum(students.values()) / len(students)
    print(f"Average Grade: {avg:.2f}\n")

def find_highest_lowest():
    if not students:
        print("No data available.\n")
        return
    
    highest = max(students, key=students.get)
    lowest = min(students, key=students.get)
    
    print(f"Highest: {highest} ({students[highest]})")
    print(f"Lowest: {lowest} ({students[lowest]})\n")

def menu():
    while True:
        print("===== Student Grade System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average")
        print("4. Highest & Lowest")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            find_highest_lowest()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")

# Run the program
menu()
