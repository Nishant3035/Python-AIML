class Student:
    def __init__(self,name,roll_no,mark):
        self.__name = name
        self.__roll_no = roll_no
        self.__mark = mark
    def to_get(self):
        print(f"Name is {self.__name} roll no is{self.__roll_no} got marks {self.__mark}")
    def set_marks(self,new_marks):
        if new_marks > 0:
            self.__mark = new_marks
            print(f"Marks is {new_marks}")
        else:
            print("Negative marks failed")
    def set_rollno(self,rollno):
        
        if rollno >0 and rollno <=100:
            self.__roll_no = rollno
            print(f"RollNo is {rollno}")
        else:
            print("Invalid RollNo")
    def set_name(self,new_name):
        
        if new_name == "":
            
            print("Name cannot be empty")
        else:
            self.__name =new_name
            print(new_name)

s1 = Student("Nishant",76,10)
s1.set_name("")      # Name cannot be empty
s1.set_name("Nish")  # Name updated to Nish
s1.to_get()          # Nish dikhna chahiye


