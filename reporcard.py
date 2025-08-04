class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def generate_report_card(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")

def main():
    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    student = Student(student_name, roll_number)

    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        marks = float(input(f"Enter marks for {subject}: "))
        student.add_marks(subject, marks)

    student.generate_report_card()

if __name__ == "__main__":
    main()