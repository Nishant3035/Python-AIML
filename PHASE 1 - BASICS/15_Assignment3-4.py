student = {}

while True:
    print("\nA - Add student")
    print("B - Update marks")
    print("C - Search student")
    print("D - Display all")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks

    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in student:
            marks = int(input("Enter new marks: "))
            student[name] = marks
        else:
            print("Student not found")

    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in student:
            print("Marks:", student[name])
        else:
            print("Student not found")

    elif choice == 'D':
        if len(student) == 0:
            print("No data available")
        else:
            for key in student:
                print(key, ":", student[key])

    elif choice == 'E':
        break

    else:
        print("Invalid choice")