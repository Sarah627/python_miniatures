from students import Student
from sortinghat import Hat


def main():
    Hat.sort()
    try:
        student = Student.get_student()
        print(student)
    except ValueError:
        print("Missing Name or House")
    # student.house = "Number Four, Privet Drive "


if __name__ == "__main__":
    main()
