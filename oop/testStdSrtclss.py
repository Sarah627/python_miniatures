from students import Student
from sortinghat import Hat


def main():
    Hat.sort()
    student = Student.get_student()
    # student.house = "Number Four, Privet Drive "
    print(student)


if __name__ == "__main__":
    main()
