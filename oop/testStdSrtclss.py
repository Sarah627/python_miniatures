from students import Student
from wizard import Wizard
from sortinghat import Hat


def main():
    # Super Class
    wizard = Wizard("Albus").define_wiz()
    Hat.sort()
    try:
        # Subclass of Suprt Class "Wizart"
        student = Student.get_student()
        print(student)
    except ValueError:
        print("Missing Name or House or wrong house name")


    # student.house = "Number Four, Privet Drive "
if __name__ == "__main__":
    main()
