Code: 
import os

FILE_NAME = "students.txt"

# Create file if not exists
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            pass

# Add student
def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(name + "," + marks + "\n")

    print("Student added successfully!\n")

# View students
def view_students():
    with open(FILE_NAME, "r") as f:
        data = f.readlines()

    if not data:
        print("No records found.\n")
        return

    print("\n--- Student Records ---")
    for line in data:
        name, marks = line.strip().split(",")
        print(f"Name: {name}, Marks: {marks}")
    print()

# Search student
def search_student():
    search_name = input("Enter name to search: ")
    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            if name.lower() == search_name.lower():
                print(f"Found -> Name: {name}, Marks: {marks}\n")
                found = True

    if not found:
        print("Student not found.\n")

# Update student
def update_student():
    search_name = input("Enter name to update: ")
    updated = False
    new_data = []

    with open(FILE_NAME, "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            if name.lower() == search_name.lower():
                new_marks = input("Enter new marks: ")
                new_data.append(name + "," + new_marks + "\n")
                updated = True
            else:
                new_data.append(line)

    with open(FILE_NAME, "w") as f:
        f.writelines(new_data)

    if updated:
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

# Delete student
def delete_student():
    search_name = input("Enter name to delete: ")
    deleted = False
    new_data = []

    with open(FILE_NAME, "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            if name.lower() != search_name.lower():
                new_data.append(line)
            else:
                deleted = True

    with open(FILE_NAME, "w") as f:
        f.writelines(new_data)

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

# Menu
def menu():
    create_file()

    while True:
        print("===== Student File System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")