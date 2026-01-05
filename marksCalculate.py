class Student:
    def __init__(self, name, age, email, address, roll_no):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.roll_no = roll_no
        self.subjects = {}   

    def add_subject(self, subject_name, marks):
        self.subjects[subject_name] = marks

    def calculate_average(self):
        if len(self.subjects) == 0:
            return 0
        total = sum(self.subjects.values())
        return total / len(self.subjects)

    def info(self):
        print("\n----- Student Info -----")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Email    : {self.email}")
        print(f"Address  : {self.address}")
        print(f"Roll No  : {self.roll_no}")
        print("Subjects and Marks:")
        for subject, marks in self.subjects.items():
            print(f"  {subject}: {marks}")
        print("Average  :", self.calculate_average())


 
if __name__ == "__main__":
    # Input about  student 
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    address = input("Enter address: ")
    roll_no = input("Enter roll number: ")

    student = Student(name, age, email, address, roll_no)
 
    num_subjects = int(input("How many subjects? "))
    for i in range(1, num_subjects + 1):
        subject_name = input(f"Enter name of subject {i}: ")
        marks = float(input(f"Enter marks for {subject_name}: "))
        student.add_subject(subject_name, marks)


  
    student.info()
