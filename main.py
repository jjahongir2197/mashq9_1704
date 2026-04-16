class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def show_subjects(self):
        print(self.name, "fanlari:")
        for sub in self.subjects:
            print("-", sub)


class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            student.show_subjects()


def main():
    s1 = Student("Ali")

    s1.add_subject("Python")
    s1.add_subject("Math")

    uni = University()

    uni.add_student(s1)

    uni.show_students()


main()
