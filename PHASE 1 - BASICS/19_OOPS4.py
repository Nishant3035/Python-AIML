class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_rollno(roll_no)
        self.set_marks(marks)

    # Setter for name
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Invalid name")
            self.__name = "Unknown"

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for roll number
    def set_rollno(self, rollno):
        if 1 <= rollno <= 100:
            self.__rollno = rollno
        else:
            print("Invalid roll number")
            self.__rollno = 0

    # Getter for roll number
    def get_rollno(self):
        return self.__rollno

    # Setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks")
            self.__marks = 0

    # Getter for marks
    def get_marks(self):
        return self.__marks


# Taking input from user
name = input("Enter name: ")
roll = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

# Creating object
s1 = Student(name, roll, marks)

# Displaying data
print("\nStudent Details:")
print("Name:", s1.get_name())
print("Roll No:", s1.get_rollno())
print("Marks:", s1.get_marks())