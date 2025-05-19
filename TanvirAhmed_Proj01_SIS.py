# Student Information System (SIS)
def add_student(students):
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Error: Student ID already exists!")
        return
    name = input("Enter Student Name: ")
    score = int(input("Enter Student Score (0-100): "))
    contact = input("Enter Contact Number: ")
    students[student_id] = {"name": name, "score": score, "contact": contact}
    print(f"Student {name} added successfully!")

def view_all_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No students found!")
        return
    print("ID\tName\tScore\tContact")
    print("-" * 40)
    for student_id, info in students.items():
        print(f"{student_id}\t{info['name']}\t{info['score']}\t{info['contact']}")

def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        info = students[student_id]
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Score: {info['score']}")
        print(f"Contact: {info['contact']}")
    else:
        print("Student not found!")

def update_student(students):
    print("\n--- Update Student Info ---")
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student not found!")
        return
    print("1. Update Score")
    print("2. Update Contact")
    choice = input("Enter choice (1-2): ")
    if choice == "1":
        new_score = int(input("Enter new score (0-100): "))
        students[student_id]["score"] = new_score
        print("Score updated successfully!")
    elif choice == "2":
        new_contact = input("Enter new contact number: ")
        students[student_id]["contact"] = new_contact
        print("Contact updated successfully!")
    else:
        print("Invalid choice!")

def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def pass_fail_list(students):
    print("\n--- Pass/Fail List ---")
    passing = []
    failing = []
    for student_id, info in students.items():
        if info["score"] >= 40:
            passing.append((student_id, info["name"], info["score"]))
        else:
            failing.append((student_id, info["name"], info["score"]))
    
    print("\nPassing Students (Score >= 40):")
    if passing:
        for student_id, name, score in passing:
            print(f"ID: {student_id}, Name: {name}, Score: {score}")
    else:
        print("No passing students!")
        
    print("\nFailing Students (Score < 40):")
    if failing:
        for student_id, name, score in failing:
            print(f"ID: {student_id}, Name: {name}, Score: {score}")
    else:
        print("No failing students!")

def main():
    students = {}
    while True:
        print("\n=== Student Information System ===")
        print("=== By Tanvir Ahmed ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Info")
        print("5. Delete Student")
        print("6. Show Pass/Fail List")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            pass_fail_list(students)
        elif choice == "7":
            print("Thank you for using Student Information System!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start the program
main()
