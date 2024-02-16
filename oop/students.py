class Student:
    # applying abstraction and encapsulation
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Syltherin", "Hafflbuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.name = name  # attributes
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("What's your name? ")
    house = input("What's your house? ")
    try:
        return Student(name, house)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
