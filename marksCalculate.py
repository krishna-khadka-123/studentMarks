class Student:
    def __init__(self, name, age, email, address, roll_no):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.roll_no = roll_no
        self.subjects = {}

    def add_subject(self, subject_name, marks):
        if 0 <= marks <= 100:
            self.subjects[subject_name] = marks
        else:
            print(" Enter marks between 0 and 100")

    def calculate_avg(self):
        if len(self.subjects) == 0:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def calculate_grade(self):
        avg = self.calculate_avg()
        if avg > 90 and avg <=100:
            return "A+"
        elif avg >= 80 and avg<=90:
            return "A"
        elif avg >= 70 and avg<=80:
            return "B+"
        elif avg >= 60 and avg<=70:
            return "B"
        elif avg >= 50 and avg<=60:
            return "C"
        else:
            return "F"

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
        print(f"Average  : {self.calculate_avg():.2f}")
        print(f"Grade    : {self.calculate_grade()}")


 
if __name__ == "__main__":
    all_students = []

    while True:
        print("\n-------------Enter Student Details--------")
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        address = input("Enter address: ")
        roll_no = input("Enter roll number: ")

        student = Student(name, age, email, address, roll_no)

        num_subjects = int(input("How many subjects? "))
        for i in range(1, num_subjects + 1):
            subject_name = input(f"Enter subject {i} name: ")
            marks = float(input(f"Enter marks for {subject_name}: "))
            student.add_subject(subject_name, marks)

        all_students.append(student)

        choice = input("Do you want to add another student? (y/n): ").lower()
        if choice != "y":
            break

    print("\n*------------STUDENTS-----------")
    total_class_average = 0
    topper = None
    highest_avg = 0

    for s in all_students:
        s.info()
        avg = s.calculate_avg()
        total_class_average += avg

        if avg > highest_avg:
            highest_avg = avg
            topper = s

    if len(all_students) > 0:
        print("\n  -----------------Class Toper")
        print(f"Class Average: {total_class_average / len(all_students):.2f}")
        print(f"Topper       : {topper.name} ({highest_avg:.2f})")
